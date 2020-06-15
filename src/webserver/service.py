from bottle import *
from sys import argv
import generator

@route('/')
def index():
	response.content_type = 'text/html'
	return static_file("index.html", root="src/webserver/html/")

@route('/random')
def get_random():
	response.content_type = 'application/json'

	generate = generator.Generator()
	setning = generate.bua_til_setningu()
	return '{"text":"' + setning + '"}'

@error(404)
def error(err):
	return "404 error, page not found!"
def main(args):
	port = 8080
	if len(args):
		port = args[0]
	run(host='0.0.0.0', port=port, debug=True)
if __name__ == '__main__':

	main(argv[1:])