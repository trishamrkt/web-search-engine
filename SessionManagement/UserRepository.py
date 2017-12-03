from User import *;

class UserRepository():
    
    def __init__(self):
        self.__user_table = {};
        
    def getAllUsers(self): 
        users = [];
        for key, value in self.__user_table.iteritems():
            users.append(value);
        return users;
    
    def getOne(self):
        for key, value in self.__user_table.iteritems():
            return key, value;
        
    def getUserById(self, id):
        if id in self.__user_table:
            return self.__user_table[id];
        else:
            print 'User Id: ' + str(id) + ' not found in UserRepository!'
            return None;
        
    def addUser(self, id, user):
        self.__user_table[id] = user;
        
    def deleteUser(self, id):
        del self.__user_table[id];
        
    def createAndSaveUser(self, username):
        if username not in self.__user_table:
            print 'Saving user: ' + username;
            user = User();
            user.setUserInfo(username);
            self.__user_table[username] = user;
        else:
            print 'User already exists in database, updating current user'
            user = self.__user_table[username];
            user.setUserInfo(username);
