from bottle import route, template, run

@route('/')
def helloagain(name='World'):
    return template('helloworld', hi=name)

run(host='localhost', port=8000, debug=True)
