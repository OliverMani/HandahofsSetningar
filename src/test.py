from sys import argv

import requests
import random
import json

from webserver.generator import Generator

"""
example: {no:NFETgr:kyn1=kyn} {so:GM-FH-NT-1P-ET} {lo:FSB-{kyn1}-NFET}
"""
def taeta(file='resources/ordalisti.csv', folder='resources/ord/'):
	with open(file, 'r', encoding='utf-8') as file:
		data = file.read()
		lines = data.split('\n')
		for line in lines:
			columns = line.split(";")
			word = columns[0]
			cat = columns[1]

			with open(folder + cat + '.txt', 'a', encoding='utf-8') as write:
				write.write(word + '\n')





def main(args):
	generate = Generator()
	print('Bý til setningu...')
	setning = generate.bua_til_setningu()
	print(setning)

if __name__ == '__main__':
	main(argv[1:])