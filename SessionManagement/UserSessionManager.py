from UserRepository import *;
from User import *;

class UserSessionManager():
    
    def __init__(self, userRepository):
        self.__userRepository = userRepository;
        self.__active_sessions = {};
        
    def getUserBySessionId(self, sessionId):
        """
        Checks if session is currently active, 
        if yes: pass the User associated with that session back
        if not: pass back None
        """
        if sessionId in self.__active_sessions:
            clientEmail = self.__active_sessions[sessionId];
            user = self.__userRepository.getUserById(clientEmail);
            return user;
        else:
            return None;
    
    def addNewSession(self, sessionId, email):
        """
        Adds new sessionId to existing active sessions
        If sessionid is already present, ignore
        """
        if sessionId not in self.__active_sessions:
            self.__active_sessions[sessionId] = email;
            return True;
        else:
            print 'SessionId already active!';
            return False;
    
    def deleteSession(self, sessionId):
        """
        Delete the session from Active Sessions list
        if Success -> return True
        if Session could not be found -> return False
        """
        if sessionId in self.__active_sessions:
            del self.__active_sessions[sessionId];
            return True;
        else:
            print 'Session deletion failed: Session specified not currently active'
            return False;
    
    def getActiveSessions(self):
        return self.__active_sessions;
        
    def getActiveUsers(self):
        """
        Returns all active users in a list
        if none exists, then returns an empty list
        """
        activeUsers = [];
        for key, value in self.__active_sessions.iteritems():
            user = self.__userRepository.getUserById();
            if user:
                activeUsers.append(user);
                
        return activeUsers;
        
    def isSessionActive(self, sessionId):
        """
        Returns True or False
        True - Session is Active
        False - Session is Inactive
        """
        return (sessionId in self.__active_sessions);
    
    