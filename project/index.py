from bottle import route, run, template, get, post, request, static_file, error
from tinydb import TinyDB, Query, where

db = TinyDB("location_of_db.json")
q = Query()

# HANDLE ERROR
@error(404)
def not_found(error):
    return "Sorry the page you were looking for was not found in our server"

# STATIC FILES
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

@route('/')
def home():
    return template('hello_template.tpl')

run(host='localhost', port=8080, debug=True)
