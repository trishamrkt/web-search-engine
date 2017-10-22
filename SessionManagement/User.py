from collections import OrderedDict

class User():

    def __init__(self):
        self.__history = {};
        self.__most_recent = {};
        self.__first_name = '';
        self.__last_name = '';


    def getHistory(self):
        return self.__history;

    def getMostRecent(self):
        return self.__most_recent;

    def getUserInfo(self):
        return self.__user_info;

    def setHistory(self, history):
        self.__history = history;

    def setMostRecent(self, most_recent):
        self.__most_recent = most_recent;

    def setUserInfo(self, user_info):
        self.__user_info = user_info;
