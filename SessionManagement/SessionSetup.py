from bottle import *
from beaker.middleware import SessionMiddleware

# Initialize session attributes
def main_app():
    session_opts = {
        'session.type' : 'cookie',
        'session.cookie_expires' : 300,
        'session.validate_key' : '1234',
        'session.auto' : True
    }

    return SessionMiddleware(app(), session_opts);
