from bottle import *
from WebScrapingServices.CrawlerService import *
from ResultsPageServices.TopTwenty import TopTwenty
from ResultsPageServices.WordData import WordData
from ResultsPageServices.SearchResultsService import SearchResultsService
from ResultsPageServices.SearchResultsHelper import SearchResultsHelper
from HTMLFormatter.HtmlHelper import *
from SessionManagement.SessionSetup import main_app
from SessionManagement.User import User
from SessionManagement.UserRepository import UserRepository
from SessionManagement.UserSessionManager import UserSessionManager
from PageRankServices.PageRankData import PageRankData
from PageRankServices.PageRankService import PageRankService
from WebScrapingServices.TextUrlData import TextUrlData
from WidgetServices.NewsWidgetService import NewsWidgetService
from WidgetServices.WeatherWidgetService import WeatherWidgetService

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2
import json
import pprint

from beaker.middleware import SessionMiddleware
from boto.cloudsearch.search import SearchResults

print ' '
print '=============================================================================================================='
print '   ____  ___   ___   ____    _    ___  '
print '  / ___|/ _ \ / _ \ / ___|  / \  / _ \ '
print ' | |  _| | | | | | | |  _  / _ \| | | |'
print ' | |_| | |_| | |_| | |_| |/ ___ \ |_| |'
print '  \____|\___/ \___/ \____/_/   \_\___/ '

print ' '
print '/\            /\      .____          .____     '
print '\ \           \ \     |    |    ____ |    |    '
print ' \ \   UofT    \ \    |    |   /  _ \|    |    '
print '  \ \           \ \   |    |__(  <_> )    |___ '
print '   \ \___________\ \  |_______ \____/|_______ \\'
print '    \/_____/_____/\/          \/             \/'
print '                                 ___      ._.  '
print '                                /  /      | |  '
print '                               /  /       |_|  '
print '                              (  (        |-|  '
print '                               \  \   /\  | |  '
print '                                \__\  \/  |_|  '
print '                                    ._.  ._.   '
print '                                    | |  | |   '
print '                                    |_|  |_|   '
print '                                    |-|  |-|   '
print '                                    | |  | |   '
print '                                    | |  | |   '
print 'Developed by: Patricia Marukot, Jimmy Li 1T9 \n\n'
print '=============================================================================================================='




textUrlData = TextUrlData();
pageRankData = PageRankData();
crawlerService = CrawlerService(textUrlData, pageRankData);
pageRankService = PageRankService(textUrlData, pageRankData);
searchResultsHelper = SearchResultsHelper();
searchResultsService = SearchResultsService(textUrlData, pageRankData, searchResultsHelper);
pageRankService.computeAllPageRank();
newsWidgetService = NewsWidgetService();
weatherWidgetService = WeatherWidgetService()

userRepository = UserRepository();
userSessionManager = UserSessionManager(userRepository);

flow = OAuth2WebServerFlow(client_id = 'XXX',
    client_secret='XXX',
    scope='https://www.googleapis.com/auth/plus.me https://www.googleapis.com/auth/userinfo.email',
    prompt='select_account',
    redirect_uri='http://ec2-54-174-107-175.compute-1.amazonaws.com/redirect')

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

    userRepository.createAndSaveUser(user_document);
    userSessionManager.addNewSession(session['_id'], user_document['email']);
    redirect('/');

@route('/')
def render_home_page():
    session = request.environ.get('beaker.session')
    username = userSessionManager.getSessionUsername(session['_id'])

    if 'signed_in' not in session or not userSessionManager.isSessionActive(session['_id']):
        session['signed_in'] = False

    if request.query_string == '' or not request.query['keywords'].strip():
        return template('index', signedIn= username if session['signed_in'] else "Sign In")

@route('/googaoLogin', method='post')
def googao_session_login():
    body = json.loads(request.body.read())
    username = body['username'];

    if userRepository.getUserById(username) != None:
        userSessionManager.setSessionActive(request.environ.get('beaker.session'), username);
        return json.dumps({'username':username, 'success':True});
    else:
        # Return username and success/failure
        return json.dumps({'username':username, 'success':False});

    print userSessionManager.getActiveSessions();

@route('/googaoSignup', method='post')
def googao_session_signup():
    body = json.loads(request.body.read())
    username = body['username'];

    # Check if username is taken
    if userRepository.getUserById(username) != None:
        return json.dumps({'username':username, 'message':'Username already taken', 'success':False});
    else:
        userRepository.createAndSaveUser(username);
        userSessionManager.setSessionActive(request.environ.get('beaker.session'), username);
        return json.dumps({'username':username, 'message':'', 'success':True});

    print userSessionManager.getActiveSessions();

@route('/logout')
def stop_session():
    session = request.environ.get('beaker.session');
    userSessionManager.deleteSession(session['_id']);
    session.invalidate();
    session['signed_in'] = False;
    redirect('/');

@route('/query', method='post')
def ajax_test():
    session = request.environ.get('beaker.session');
    body = json.loads(request.body.read())
    keywords = body['keywords'];

    if userSessionManager.isSessionActive(session['_id']):
        user = userSessionManager.getUserBySessionId(session['_id']);
        user.setLastSearched(keywords);

    keywords = searchResultsHelper.extract_keywords(keywords);
    keywords = searchResultsHelper.lower_case(keywords);
    result = searchResultsService.find_word(keywords);
    time = result[1];
    print "Time taken: " + str(time) + 'ms';

    split_results = searchResultsService.get_return_results(result[0])
    return json.dumps(split_results)

@route('/gethistory', method='post')
def get_history():
    session = request.environ.get('beaker.session');

    if session['signed_in'] != None and session['signed_in']:
        return_json = {};
        user = userSessionManager.getUserBySessionId(session['_id']);
        signed_in_data = signed_in_results(user.getLastSearched(), user.getHistory(), user.getMostRecent(), user.getUsername());

        user.setHistory(signed_in_data[1]);
        user.setMostRecent(signed_in_data[2]);
        return_json[0] = [x[0] for x in sorted(user.getHistory().items(), key=lambda(k,v):(v,k), reverse=True)];
        return_json[1] = ordered_dict_to_array(user.getMostRecent());

        return json.dumps(return_json);
    else:
        return json.dumps({});

@route('/getimages', method='post')
def get_images():

    # Request payload: search_results in arrays of 5
    body = json.loads(request.body.read());
    pprint.pprint(body['search_results']);
    urls = concat_arrays(body['search_results']);

    # Returns array of urls for images from order of priority
    image_urls = crawlerService.get_images_from_urls(urls);
    unique_urls = crawlerService.make_unique(image_urls)
    return json.dumps(unique_urls);

@route('/getnews', method="post")
def get_news():
    articles = newsWidgetService.get_news();
    return json.dumps(articles);

@route('/getweather', method="POST")
def get_weather():
    forecast = weatherWidgetService.get_forecast_by_region("toronto")
    return json.dumps(forecast)

@route('/lab1unittest')
def lab1_unit_test():
    return template('lab1unittest')

@route('/lab1unittest2')
def lab1_unit_test2():
    return template('lab1unittest2')

@error(404)
def error_handler_404(error):
    return template('error404')

@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

@get ('/static/Images/<filepath:re:.*\.png>')
def static_img(filepath):
    return static_file(filepath, root='static/Images')

@get ('/static/js/<filepath:re:.*\.js>')
def static_js(filepath):
    return static_file(filepath, root="static/js")

@get ('/static/js/GoogaoAngularApp/<filepath:re:.*\.js>')
def static_js_angular(filepath):
    return static_file(filepath, root="static/js/GoogaoAngularApp")

@get ('/static/js/GoogaoAngularApp/Templates/<filepath:re:.*\.html>')
def static_js_angular(filepath):
    return static_file(filepath, root="static/js/GoogaoAngularApp/Templates")

if __name__ == '__main__':
    TEMPLATE_PATH.insert(0,'./views/unittest/')
    run(app=app, host='localhost', port=8000, debug=True);
