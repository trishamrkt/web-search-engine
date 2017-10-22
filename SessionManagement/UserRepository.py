
class UserRepository():
    
    def __init__(self):
        self.__user_table = {};
        
    def getUserById(self, id):
        # id is user's email
        return self.__user_table['id'];
    
    def addUser(self, id, user):
        self.__user_table[id] = user;
        
    