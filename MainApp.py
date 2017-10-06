from bottle import *
from WebScrapingServices.CrawlerService import *
from ResultsPageServices.TopTwenty import TopTwenty
from ResultsPageServices.WordData import WordData
from HTMLFormatter.HtmlHelper import results_html

crawlerService = CrawlerService();
mostPopular = TopTwenty();

@route('/')
def root_path():
    if request.query_string == '' or not request.query['keywords'].strip():
        return template('index')
    else:
        return results_html(request.query['keywords'].lower(), mostPopular);

@route('/lab1unittest')
def lab1_unit_test():
    return template('lab1unittest')

@route('/lab1unittest2')
def lab1_unit_test2():
    return template('lab1unittest2')

@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

@get ('/static/Images/<filepath:re:.*\.png>')
def static_img(filepath):
    return static_file(filepath, root='static/Images')

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True);
