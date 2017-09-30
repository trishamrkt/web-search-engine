from bottle import *

@route('/')
def root_path():
    return template('index')

run(host='localhost', port=8000, debug=True);
