from bottle import *
from WebScrapingServices.CrawlerService import *
from ResultsPageServices.TopTwenty import TopTwenty
from ResultsPageServices.WordData import WordData
from HTMLFormatter.HtmlHelper import *
from SessionManagement.SessionSetup import main_app
from SessionManagement.User import User
from SessionManagement.UserRepository import UserRepository
from SessionManagement.UserSessionManager import UserSessionManager

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2

from beaker.middleware import SessionMiddleware

crawlerService = CrawlerService();

userRepository = UserRepository();
userSessionManager = UserSessionManager(userRepository);


flow = OAuth2WebServerFlow(client_id = 'XXX',
    client_secret='XXX',
    scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email',
    prompt='select_account',
    redirect_uri='http://localhost:8000/redirect')

app = main_app();

@route('/login')
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

    http = httplib2.Http();
    http = credentials.authorize(http);
    users_service = build('oauth2', 'v2', http=http);
    user_document = users_service.userinfo().get().execute();

    _id = session['_id'];
    email = user_document['email'];
    userRepository.createAndSaveUser(email, user_document);
    userSessionManager.addNewSession(_id, email);

    users = userSessionManager.getActiveUsers();
    for u in users:
        print u.getUserInfo()['email'] + ' | ';

    redirect('/');


@route('/')
def render_home_page():
    session = request.environ.get('beaker.session')
    if 'signed_in' not in session or not userSessionManager.isSessionActive(session['_id']):
        session['signed_in'] = False

    if request.query_string == '' or not request.query['keywords'].strip():
        return template('index', signedIn= userSessionManager.getUserEmail(session['_id']) if session['signed_in'] else "Sign In")

    # Check for Anonymous mode and Signed_in Mode
    else:
        search_string = request.query['keywords'].lower()
        if session['signed_in']:
            user = userSessionManager.getUserBySessionId(session['_id']);
            signed_in_data = signed_in_results(search_string, user.getHistory(), user.getMostRecent());
            user.setHistory(signed_in_data[1]);
            user.setMostRecent(signed_in_data[2])
            return signed_in_data[0];
        else:
            return anonymous_results(search_string);

@route('/logout')
def stop_session():
    session = request.environ.get('beaker.session');
    userSessionManager.deleteSession(session['_id']);
    session.invalidate();
    session['signed_in'] = False;
    redirect('/')

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

@get ('/static/js/<filepath:re:.*\.js>')
def static_js(filepath):
    return static_file(filepath, root="static/js")

if __name__ == '__main__':
    TEMPLATE_PATH.insert(0,'./views/unittest/')
    run(app=app, host='localhost', port=8000, debug=True);
