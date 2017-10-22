
class UserSessionManager():
    
    def __init__(self):
        self.__active_sessions = {};
        
    def getUserBySessionId(self, sessionId):
        return None;
    
    def addNewSession(self, sessionId, email):
        return None;
    
    def deleteSession(self, sessionId):
        return False;
    
    def getActiveSessions(self):
        return self.__active_sessions;
    
    def isSessionActive(self, sessionId):
        return False;