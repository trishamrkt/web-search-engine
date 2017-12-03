from collections import OrderedDict

class User():

    def __init__(self, username):
        self.__history = OrderedDict();
        self.__most_recent = OrderedDict();
        self.__first_name = '';
        self.__last_name = '';
        self.__last_searched = '';
        self.__username = username;

    def getHistory(self):
        return self.__history;

    def getMostRecent(self):
        return self.__most_recent;
    
    def getUserInfo(self):
        return self.__user_info;
    
    def getUsername(self):
        return self.__username;
    
    def getLastSearched(self):
        return self.__last_searched;
    
    def setLastSearched(self, last_searched):
        self.__last_searched = last_searched;
        
    def setUsername(self, username):
        self.__username = username;
        
    def setHistory(self, history):
        self.__history = history;

    def setMostRecent(self, most_recent):
        self.__most_recent = OrderedDict(most_recent);

    def setUserInfo(self, user_info):
        self.__user_info = OrderedDict(user_info);
