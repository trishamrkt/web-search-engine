from bottle import *
from crawlerservice.Crawler import *

crawler = Crawler();

# ROOT PATH OF APPLICATION
@route('/')
def root_path():
    crawler.get_resolved_inverted_index();
    return template('index')

# QUERY ENDPOINTS
@route('/query')
def query_path():
    return
    
# STATIC IMPORT FILES
@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
