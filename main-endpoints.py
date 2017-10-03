from bottle import *
from crawlerservice.CrawlerService import *
from toptwenty.toptwenty import TopTwenty
from toptwenty.word_data import WordData
from HTMLFormatter.html_helper import results_html

crawlerService = CrawlerService();
mostPopular = TopTwenty();

@route('/')
def root_path():
    if request.query_string == '':
        return template('index')
    else:
        return results_html(request.query['keywords'].lower(), mostPopular);


@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
