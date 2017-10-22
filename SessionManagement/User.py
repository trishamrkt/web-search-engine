
class User():
    
    def __init__(self):
        self.__history = [];
        self.__first_name = '';
        self.__last_name = '';
        
    
    def getHistory(self):
        return self.__history;
    
    def getUserInfo(self):
        return self.__user_info;
    
    def setHistory(self, history):
        self.__history = history;
        
    def setUserInfo(self, user_info):
        self.__user_info = user_info;