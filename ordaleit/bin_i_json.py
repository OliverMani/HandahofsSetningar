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


class MainClass:

	

	def append_data(self, data):
		listi = {}
		flokkur = data[0].get('ofl')
		kyn = data[0].get('kyn')
		


	def main(self, args):
		self.listi = Uppsetning('resources/ord.json')

		word = ""
		if len(args) > 0:
			word = args[0]
		else:
			word = input("Sláðu inn nafnorð: ")
		r = requests.get("https://bin.arnastofnun.is/api/ord/" + word)
		print(r.status_code)
		data = json.loads(r.content)
		print(data)
		if len(data) > 1:
			for x in range(len(data)):
				guid = data[x].get('guid')
				new_r = requests.get("https://bin.arnastofnun.is/api/ord/" + guid)
				self.append_data(new_r.content)
		else:
			self.append_data(data)
		print(len(data))


if __name__ == '__main__':
	mainc = MainClass()
	mainc.main(argv[1:])