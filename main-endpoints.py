from bottle import *

TEMPLATE_PATH.insert(0,'/views/css');

@route('/')
def root_path():
    return template('index')

run(host='localhost', port=8000, debug=True);
