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
            return self.__user_table['id'];
        else:
            print 'User Id: ' + str(id) + ' not found in UserRepository!'
            return None;
        
    def addUser(self, id, user):
        self.__user_table[id] = user;
        
    def deleteUser(self, id):
        del self.__user_table[id];