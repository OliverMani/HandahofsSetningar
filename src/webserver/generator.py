import requests
import random
import json

class Generator:
	def __init__(self, mappa='resources/ord/', setningar='resources/setningar.txt'):
		self.stillingar = {}
		self.setningar = setningar
		self.mappa = mappa

	def finna_setningu(self):
		skra = open(self.setningar, 'r', encoding='utf-8')
		linur = skra.read().split('\n')
		skra.close()
		return linur[random.randint(0, len(linur))-1]

	def bua_til_setningu(self):
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

	def fa_ord(self, kodi):
		if kodi[0] != '{' or kodi[-1] != '}':
			return kodi
		gogn = kodi[1:-1]
		for key, value in self.stillingar.items():
			gogn = gogn.replace('{' + key + '}', value['ord'])

		flokkur = gogn.split(':')[0]
		mynd = gogn.split(':')[1]
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
				prufa = listi[random.randint(0, len(listi))]
				fyrirspurn = requests.get('https://bin.arnastofnun.is/api/ord/' + prufa)
				svar = json.loads(fyrirspurn.content)
				#print("Syndax:", gogn)
				if type(svar) == list:
					kyn = svar[0]['kyn']
					for x in self.stillingar.keys():
						if not self.stillingar[x]['notad']:
							if self.stillingar[x]['ord'] == 'kyn':
								self.stillingar[x]['notad'] = True
								self.stillingar[x]['ord'] = kyn
					
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