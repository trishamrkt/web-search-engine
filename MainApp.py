from bottle import *
from WebScrapingServices.CrawlerService import *
from ResultsPageServices.TopTwenty import TopTwenty
from ResultsPageServices.WordData import WordData
from HTMLFormatter.HtmlHelper import results_html

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

crawlerService = CrawlerService();
mostPopular = TopTwenty();

flow = OAuth2WebServerFlow(client_id = 'CLIENT_ID',
    client_secret='CLIENT_SECRET',
    scope='https://www.googleapis.com/auth/plus.me',
    redirect_uri='http://localhost:8000/redirect')

@route('/')
def root_path():
    # flow = flow_from_clientsecrets("client_secret.json",
    # scope='https://www.googleapis.com/auth/plus.me',
    # redirect_uri="http://localhost:8000/redirect")

    uri = flow.step1_get_authorize_url();
    print "uri: " + str(uri);
    redirect(str(uri));

    # if request.query_string == '' or not request.query['keywords'].strip():
    #     return template('index')
    # else:
    #     return results_html(request.query['keywords'].lower(), mostPopular);


@route('/redirect')
def redirect_page():
    code = request.query.get('code','')
    # flow = OAuth2WebServerFlow(client_id = 'xxx',
    #     client_secret='xxx',
    #     scope='https://www.googleapis.com/auth/plus.me',
    #     redirect_uri='http://localhost:8000/redirect')
    credentials = flow.step2_exchange(code)
    token = credentials.id_token['sub']

    redirect('/home');


@route('/home')
def render_home_page():
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
    TEMPLATE_PATH.insert(0,'./views/unittest/')
    run(host='localhost', port=8000, debug=True);
