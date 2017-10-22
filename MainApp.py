from bottle import *
from WebScrapingServices.CrawlerService import *
from ResultsPageServices.TopTwenty import TopTwenty
from ResultsPageServices.WordData import WordData
from HTMLFormatter.HtmlHelper import results_html
from SessionManagement.SessionSetup import main_app

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2

from beaker.middleware import SessionMiddleware

crawlerService = CrawlerService();
mostPopular = TopTwenty();

flow = OAuth2WebServerFlow(client_id = 'XXX',
    client_secret='XXX',
    scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email',
    prompt='select_account',
    redirect_uri='http://localhost:8000/redirect')

app = main_app();

@route('/')
def root_path():
    uri = flow.step1_get_authorize_url();
    redirect(str(uri));


@route('/redirect')
def redirect_page():
    code = request.query.get('code','')
    credentials = flow.step2_exchange(code)
    token = credentials.id_token['sub']

    session = request.environ.get('beaker.session')
    session['access_token'] = token;
    session['signed_in'] = True;

    # get user info
    http = httplib2.Http()
    http = credentials.authorize(http)

    # get user email
    users_service = build('oauth2', 'v2', http=http);
    user_document = users_service.userinfo().get().execute()
    user_email = user_document['email']

    redirect('/home');


@route('/home')
def render_home_page():
    if request.query_string == '' or not request.query['keywords'].strip():
        return template('index')
    else:
        return results_html(request.query['keywords'].lower(), mostPopular);

@route('/logout')
def stop_session():
    session = request.environ.get('beaker.session');
    session.invalidate();
    session['signed_in'] = False;
    redirect('/home')

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

@get ('/static/js/<filepath:re:.*\js>')
def static_js(filepath):
    return static_file(filepath, root="static/js")

if __name__ == '__main__':
    TEMPLATE_PATH.insert(0,'./views/unittest/')
    run(app=app, host='localhost', port=8000, debug=True);
