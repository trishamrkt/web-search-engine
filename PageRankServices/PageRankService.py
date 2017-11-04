import numpy as np
from PageRankData import PageRankData

class PageRankService():

    def __init__(self, __textUrlData, __pageRankData):
        self.__textUrlData = __textUrlData;
        self.__pageRankData = __pageRankData;
        self.__inbound = self.__pageRankData.getInbound();
        self.__outbound = self.__pageRankData.getOutbound();
        self.__page_rank = self.__pageRankData.getPageRank();
        self.__num_links = self.__pageRankData.getNumLinks();

        for url in __textUrlData.getDocId_to_url():
            self.__page_rank[url] = 1;

    # Accessors
    def getPageRankData(self):
        return self.__pageRankData;

    # Compute page rank algorithm for the given url
    # Equation: PR(url) = (1 - d) + d*(P(T1)/C(T1)+...+P(n)/C(n))
    def computePageRank(self, url, num_iterations=20, damping_factor=0.85):
        lead = 1.0 - damping_factor

        # Links with no inbound urls
        if len(self.__inbound[url]) == 0:
            return lead;

        # Perform 20 iterations of algorithm
        for i in range(num_iterations):

            # Loop through all the links that point to url
            # Compute its pagerank and set its value accordingly in page_rank ds
            for link in self.__inbound[url]:
                # Compute P(T1)/C(T1), P(T2)/C(T2), ... , P(Tn)/C(Tn)
                if len(self.__inbound[link]) != 0:
                    partial_page_ranks = [float(self.__page_rank[l])/float(self.__num_links[l]) for l in self.__inbound[link]]
                    current_pagerank = damping_factor*(sum(partial_page_ranks))
                    page_rank = lead + current_pagerank
                else:
                    page_rank = lead

                self.__page_rank[link] = page_rank;

        # Compute final page rank score of url
        self.__page_rank[url] = lead + damping_factor*sum([float(self.__page_rank[l])/self.__num_links[l] for l in self.__inbound[url]])

        print self.__page_rank[url]
        return self.__page_rank[url]
