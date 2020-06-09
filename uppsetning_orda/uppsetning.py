import json

from sys import argv

class Uppsetning:
	def __init__(self, path):
		self.path = path
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


def main(args):
	pass

if __name__ == '__main__':
	main(args[1:])