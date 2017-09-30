from bottle import *

TEMPLATE_PATH.insert(0,'/views/css');

@route('/')
def root_path():
    return template('index')

@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
