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
		komid = list(self.listi.data['no'].keys())
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
			print("Orði bætt við!")

		elif flokkur == "so":
			pass
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