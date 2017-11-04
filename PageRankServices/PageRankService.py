from PageRankData import PageRankData

class PageRankService():
    
    def __init__(self):
        self.__pageRankData = PageRankData();
        
    def getPageRankData(self):
        return self.__pageRankData;