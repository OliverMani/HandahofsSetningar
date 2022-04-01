import requests
import random
import json

class BINDownException(Exception):
	def __init__(self, msg='BIN down'):
		self.message = msg

class Generator:
	def __init__(self, mappa='resources/ord/', setningar='resources/setningar.txt'):
		self.stillingar = {}
		self.setningar = setningar
		self.mappa = mappa
		self.personur = {
			'1P':['ég', 'vér'],
			'2P':['þú', 'þér'],
			'3P':['hann', 'hún', 'það']
		}


	def finna_setningu(self):
		skra = open(self.setningar, 'r', encoding='utf-8')
		linur = skra.read().split('\n')
		skra.close()
		return linur[random.randint(0, len(linur))-1]

	def bua_til_setningu(self):
		try:
			setning = self.finna_setningu().split(' ');
			nidurstada = ""
			for x in setning:
				_ord = self.fa_ord(x)
				while _ord == None:
					_ord = self.fa_ord(x)
				nidurstada += _ord + " "
			stor_stafur = list(nidurstada)
			stor_stafur[0] = stor_stafur[0].upper()
			nidurstada = ''.join(stor_stafur)
			return nidurstada[:-1] + "."
		except BINDownException as e:
			print("BIN DOWN")
			return e.message

	def fa_ord(self, kodi):

		kodi2 = kodi.replace('.','').replace(',','')
		#print(kodi, "kodi2:", kodi2)
		if kodi2[0] != '{' or kodi2[-1] != '}':
			return kodi
		gogn = kodi[kodi.index('{') + 1:(len(kodi) - kodi[::-1].index('}'))-1]
		for key, value in self.stillingar.items():
			gogn = gogn.replace('{' + key + '}', value['ord'])

		flokkur = gogn.split(':')[0]
		mynd = gogn.split(':')[1]

		#print("Stillingar:", self.stillingar)
		if len(gogn.split(':')) > 2:
			lykill = gogn.split(':')[2].split("=")[0]
			gildi = gogn.split(':')[2].split("=")[1]

			self.stillingar[lykill] = {'ord':gildi,'notad':False}

		# Svo þurfum við að velja random orð
		_ord = ""
		with open(self.mappa + flokkur + '.txt', 'r', encoding='utf-8') as skra:
			allt = skra.read()
			listi = allt.split("\n")
			while True:
				prufa = listi[random.randint(0, len(listi)-1)]
				fyrirspurn = requests.get('https://bin.arnastofnun.is/api/ord/' + prufa)
				if fyrirspurn.status_code >= 500:
					raise BINDownException("Villa: Þjónusta Árnastofnunar liggur niðri, vinsamlegast reynið aftur síðar!")
				svar = json.loads(fyrirspurn.content)
				#print("Syndax:", gogn)
				if type(svar) == list:
					kyn = svar[0]['kyn']
					for x in self.stillingar.keys():
						if not self.stillingar[x]['notad']:
							if self.stillingar[x]['ord'] == 'kyn':
								self.stillingar[x]['notad'] = True
								self.stillingar[x]['ord'] = kyn
							if flokkur == 'pfn' and self.stillingar[x]['ord'] == 'persona':
								#print("Persónufornafn:", svar[0].get('bmyndir'))
								if svar[0].get('bmyndir')[0].get('b') in self.personur['1P']:
									self.stillingar[x]['notad'] = True
									self.stillingar[x]['ord'] = '1P'
								elif svar[0].get('bmyndir')[0].get('b') in self.personur['2P']:
									self.stillingar[x]['notad'] = True
									self.stillingar[x]['ord'] = '2P'
								elif svar[0].get('bmyndir')[0].get('b') in self.personur['3P']:
									self.stillingar[x]['notad'] = True
									self.stillingar[x]['ord'] = '3P'

					myndir = svar[0].get('bmyndir')
					if myndir == None:
						continue
					if len(list(svar[0].get('bmyndir')[0].keys())) == 0:
						return svar[0]['ord']
					x = 0
					for fall in myndir:
						if fall['g'].lower() == mynd.lower() or (flokkur == 'no' and 'gr' in mynd and prufa[0] == prufa[0].upper()):
							return svar[0]['bmyndir'][x]['b']
						#print(fall)
						x += 1
					break
