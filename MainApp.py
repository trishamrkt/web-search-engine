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

from oauth2client.client import OAuth2WebServerFlow
from oauth2client.client import flow_from_clientsecrets
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
import httplib2
import json
import pprint

from beaker.middleware import SessionMiddleware
from boto.cloudsearch.search import SearchResults

textUrlData = TextUrlData();
pageRankData = PageRankData();
crawlerService = CrawlerService(textUrlData, pageRankData);
pageRankService = PageRankService(textUrlData, pageRankData);
searchResultsHelper = SearchResultsHelper();
searchResultsService = SearchResultsService(textUrlData, pageRankData, searchResultsHelper);
pageRankService.computeAllPageRank();

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
    url1 = "https://cdn.dribbble.com/users/458522/screenshots/3886513/my_neighbor_totoroo_1x.jpg"
    url2 = "https://ggk123.files.wordpress.com/2014/05/20140523-111056-40256094.jpg"
    url3 = "https://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/250px-025Pikachu.png"
    url4 = "https://resizing.flixster.com/4Aw_njfSakDC_wbFD1IJx5U7MRY=/300x300/v1.bjsxMDcwMzA3O2o7MTc1NjI7MTIwMDs4MDA7NjAw"
    url5 = "https://ih1.redbubble.net/image.401723963.6832/st%2Csmall%2C215x235-pad%2C210x230%2Cf8f8f8.lite-1u1.jpg"
    url6 = "https://dw9to29mmj727.cloudfront.net/promo/2016/5257-SeriesHeaders_SMv3_2000x800.jpg"
    url7 = "http://vignette1.wikia.nocookie.net/dbz-dokkanbattle/images/6/68/Leaping_Even_Higher_Super_Saiyan_Goku.png/revision/latest?cb=20160830122933"
    url8 = "https://occ-0-116-114.1.nflxso.net/art/54244/272bd909045456af974c61068f168cafc3a54244.jpg"
    url9 = "https://upload.wikimedia.org/wikipedia/en/0/05/Hello_kitty_character_portrait.png"
    url10 = "https://images-na.ssl-images-amazon.com/images/I/51lK5b92Q1L._SX355_.jpg"
    url11 = "https://ae01.alicdn.com/kf/HTB1bArUPFXXXXXLXpXXq6xXFXXXc/Spirited-Away-ogino-chihiro-cosplay-costume-Halloween-anime-dress-free-shipping.jpg"
    url12 = "http://www.iralovestolaugh.com/wp-content/uploads/2015/08/Orange-Star-Icon-300x277.png"
    url13 = "https://qzprod.files.wordpress.com/2016/06/oie_transparent-28-11.png?w=641"
    url14 = "https://stickershop.line-scdn.net/stickershop/v1/product/1169/LINEStorePC/main@2x.png;compress=true"
    url15 = "https://stickershop.line-scdn.net/stickershop/v1/product/1252/LINEStorePC/main@2x.png;compress=true"
    url16 = "https://www.aldoramuses.com/wp-content/uploads/2014/02/oie_transparent-41.png"
    return json.dumps([url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12, url13, url14, url15, url16])

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
