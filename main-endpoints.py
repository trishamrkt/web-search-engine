from bottle import *
from crawlerservice.CrawlerService import *

crawlerService = CrawlerService();

# ROOT PATH OF APPLICATION
@route('/')
def root_path():
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
