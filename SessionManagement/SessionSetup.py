from bottle import *
from beaker.middleware import SessionMiddleware

from SessionManagement.UserRepository import *;
from SessionManagement.UserSessionManager import *;

# Initialize session attributes
def main_app():
    
    userRepository = UserRepository();
    userSessionManager = UserSessionManager(userRepository);
    
    session_opts = {
        'session.type' : 'cookie',
        'session.cookie_expires' : 300,
        'session.validate_key' : '1234',
        'session.auto' : True
    }

    return SessionMiddleware(app(), session_opts);
