
class PageRankData():

    def __init__(self):
        self.__inbound = {};
        self.__outbound = {};
        self.__page_rank = {};
        self.__num_links = {};

    def getInbound(self):
        return self.__inbound;

    def getOutbound(self):
        return self.__outbound;

    def getNumLinks(self):
        return self.__num_links;

    def getPageRank(self):
        return self.__page_rank;

    def setInbound(self, __inbound):
        self.__inbound.clear();
        for url, links in __inbound.iteritems():
            self.__inbound[url] = links

    def setOutbound(self, __outbound):
        self.__outbound.clear();
        for url, links in __outbound.iteritems():
            self.__outbound[url] = links

    def setNumLinks(self, __num_links):
        self.__num_links.clear();
        for url, links in __num_links.iteritems():
            self.__word_to_url[url] = lins

    def setPageRank(self, __page_rank):
        self.__page_rank.clear();
        for url, links in __page_rank.iteritems():
            self.__word_to_url[url] = links
