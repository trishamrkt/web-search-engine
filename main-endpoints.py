from bottle import *
from crawlerservice.CrawlerService import *
from toptwenty.toptwenty import TopTwenty
from toptwenty.word_data import WordData

crawlerService = CrawlerService();
most_popular = TopTwenty();

@route('/')
def root_path():
    return template('index')

@route('/query')
def word_count():
    search_string = request.query['keywords'];
    word_data = WordData();

    # Gets HTML for table with words and their word counts
    html = '<link type="text/css" rel="stylesheet" href="/static/css/word_table_data.css"\>'
    html += "<link href='https://fonts.googleapis.com/css?family=Assistant' rel='stylesheet'>"
    html = html + word_data.get_table_html(search_string, most_popular);
    html = html + most_popular.get_table_html();
    return html;

@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
