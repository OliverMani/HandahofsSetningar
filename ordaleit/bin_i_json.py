from sys import argv

import requests
import json
"""

Stucture:

{'is:' {
	'no':....
	'so':....
	'lo':....
	'ao':....
	'pfn':...
	'fn':....
	'afn':...
	'st':....
	'nhm':...
	'fs':....

}}

"""
class Uppsetning:
	def __init__(self, path, autoload=True):
		self.path = path
		if autoload:
			self.data = self.load()


	def load(self):
		file = open(self.path, 'r', encoding='utf-8')
		text = file.read()
		data = ''
		if text == '':
			return {}
		else:
			data = json.loads(text)
		file.close()
		return data
	def save(self):
		with open(self.path, 'w', encoding='utf-8') as file:
			res = json.dumps(self.data)
			file.write(res)

class Ord:
	def __init__(self, gogn):
		pass

	def to_json(self):
		return {}


class MainClass:



	def setup(self):
		pass

	def append_data(self, data):
		listi = {}
		flokkur = data[0].get('ofl')
		kyn = data[0].get('kyn')
		k = self.listi.data.get(flokkur)
		if k != None:
			komid = list(k.keys())
			if data[0]['ord'] in komid:
				print("Orðið er nú þegar þarna!")
				return

		if flokkur == "no":
			
			for mynd in data[0].get('bmyndir'):
				if listi.get('mynd') == None:
					listi['mynd'] = {}
				listi['kyn'] = data[0].get('kyn')
				fall = mynd.get('g')[0:2]
				bil = 1 if fall[1] == 'G' else 0
				tala = mynd.get('g')[2 + bil: 4 + bil]
				if bil == 1:
					fall += 'F'
				greinir = 'gr' in mynd.get('g')
				#print("Mynd:", mynd.get('b'), "fall:", fall, "tala:", tala, "greinir:", greinir)

				strgreinir = 'greinir' if greinir else 'ekki_greinir'

				if listi['mynd'].get(strgreinir) == None:
					listi['mynd'][strgreinir] = {}
				if listi['mynd'].get(strgreinir).get(tala.lower()) == None:
					listi['mynd'][strgreinir][tala.lower()] = {}


				listi['mynd'][strgreinir][tala.lower()][fall.lower()] = mynd.get('b')


				"""
				Uppbygging:
				{
					'greinir':{
						'et': {
							föll...
						},
						'ft': {
							föll...
						}
					}, 'ekki_greinir': {
						'et': {
							föll...
						},
						'ft': {
							föll...
						}
					}
				}
				"""
			#print(listi)
			if self.listi.data.get('no') == None:
				self.listi.data['no'] = {}
			self.listi.data['no'][data[0].get('ord')] = listi
			print("Nafnorði bætt við!")

		elif flokkur == "so":
			for mynd in data[0].get('bmyndir'):

				#þurfum að þátta g!
				upplysingar = {}

				g = mynd.get('g').split('-')

				myndir = ['GM', 'MM', 'LHNT', 'LHÞT'] #Germynd, Miðmynd, Lýsingarháttur nútíðar, Lýsingarþáttur þátíðar
				hattar = ['NH', 'FH', 'VH', 'BH'] # háttur, ekki hattur.... NH = , FH = Framsöguháttur, VH = viðtengingarháttur
				tidir = ['NT', 'ÞT']
				personur = ['1P', '2P', '3P']
				tolur = ['ET', 'FT']
				kyn = ['KK', 'KVK', 'HK']
				foll = ['NFET', 'ÞFET', 'ÞGFET', 'EFET', 'NFFT', 'ÞFFT, ÞGFFT', 'EFFT']
				beyging = ['SB', 'VB']
				sagnbot = ['SAGNB'] # sagnbót

				for x in g: #paring g code
					if x in myndir:
						upplysingar['mynd'] = x
					elif x in hattar:
						upplysingar['hattur'] = x
					elif x in personur:
						upplysingar['persona'] = x
					elif x in tolur:
						upplysingar['tala'] = x
					elif x in kyn:
						upplysingar['kyn'] = x
					elif x in foll:
						upplysingar['fall'] = x[:2]
						if upplysingar['fall'] == 'ÞG':
							upplysingar['fall'] += 'F'
					elif x in beyging:
						upplysingar['beyging'] = x
					elif x in sagnbot:
						upplysingar['sagnbot'] = True

				if upplysingar.get('mynd') == None:
					continue
				if upplysingar.get('hattur') == None:
					upplysingar['hattur'] = 'annad'

				if upplysingar['mynd'] in ['GM', 'MM']:
					if upplysingar['hattur'] in ['FH', 'VH']:
						upplysingar['ord'] = mynd.get('b')

						if listi.get('myndir') == None:
							listi['myndir'] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')) == None:
							listi['myndir'][upplysingar.get('mynd')] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')).get(upplysingar.get('hattur')) == None:
							listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')).get(upplysingar.get('hattur')).get(upplysingar.get('persona')) == None:
							listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')][upplysingar.get('persona')] = {}
						
						
						listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')][upplysingar.get('persona')][upplysingar.get('tala')] = upplysingar['ord']
					elif upplysingar['hattur'] == 'BH':
						upplysingar['ord'] = mynd.get('b')

						if listi.get('myndir') == None:
							listi['myndir'] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')) == None:
							listi['myndir'][upplysingar.get('mynd')] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')).get(upplysingar.get('hattur')) == None:
							listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')] = {}
						
						
						listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')][upplysingar.get('tala')] = upplysingar['ord']
					else:

						upplysingar['ord'] = mynd.get('b')

						if listi.get('myndir') == None:
							listi['myndir'] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')) == None:
							listi['myndir'][upplysingar.get('mynd')] = {}
						if listi.get('myndir').get(upplysingar.get('mynd')).get(upplysingar.get('hattur')) == None:
							listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')] = []
						
						listi['myndir'][upplysingar.get('mynd')][upplysingar.get('hattur')].append(upplysingar)
				elif upplysingar['mynd'] == 'LHNT':
					if listi.get('myndir') == None:
						listi['myndir'] = {}
					listi['myndir']['LHNT'] = mynd.get('b')
				else:
					if listi.get('myndir') == None:
						listi['myndir'] = {}
					if listi.get('myndir').get('LHÞT') == None:
						listi['myndir']['LHÞT'] = {}
					if listi.get('myndir').get('LHÞT').get(upplysingar.get('beyging')) == None:
						listi['myndir']['LHÞT'][upplysingar.get('beyging')] = {}
					if listi.get('myndir').get('LHÞT').get(upplysingar.get('beyging')).get(upplysingar.get('kyn')) == None:
						listi['myndir']['LHÞT'][upplysingar.get('beyging')][upplysingar.get('kyn')] = {}
					

					if upplysingar.get('fall') != None:
						listi['myndir']['LHÞT'][upplysingar.get('beyging')][upplysingar.get('kyn')][upplysingar.get('fall')] = mynd.get('b')
					


			if self.listi.data.get('so') == None:
				self.listi.data['so'] = {}
			self.listi.data['so'][data[0].get('ord')] = listi
			print("Sagnorði bætt við!")
		elif flokkur == "lo":
			pass


	def main(self, args):
		self.listi = Uppsetning('resources/ord.json')
		self.setup()

		word = ""
		if len(args) > 0:
			word = args[0]
		else:
			word = input("Sláðu inn nafnorð: ")
		r = requests.get("https://bin.arnastofnun.is/api/ord/" + word)
		#print(r.status_code)
		data = json.loads(r.content)
		if type(data) != list:
			print("Orð er ekki til!")
			return
			
		if len(data) > 1:
			for x in range(len(data)):
				guid = data[x].get('guid')
				new_r = requests.get("https://bin.arnastofnun.is/api/ord/" + guid)
				self.append_data(new_r.content)
		else:
			self.append_data(data)

		self.listi.save()
		


if __name__ == '__main__':
	mainc = MainClass()
	mainc.main(argv[1:])