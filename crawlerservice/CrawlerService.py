from TextUrlData import *; 
from Crawler import *;
from WebScrape import *;

# this class provides all methods for loading the data structures

class CrawlerService():
    
    def __init__(self):
        # instantiates data / service classes
        self.__textData = TextUrlData();
        self.__webscraper = WebScrape(self.__textData);
        self.__crawler = Crawler(self.__textData); 
        
        # loads all data structures by calling lower tier helper classes
        self.__generate_data_structures();


    def get_resolved_inverted_index(self): 
        inverted_index = self.__crawler.get_resolved_inverted_index();
        return inverted_index;
    
    def get_inverted_index(self):
        return self.__textData.getWordId_to_DocIds();
    
    
    # Private Helper Functions
    # Reads input file from base path of application
    def __read_input_file_helper(self, docId_to_url):
        with open('url.txt') as inputfile:
            for url in inputfile:
                if not self.__is_doc_already_scanned(url.strip(), docId_to_url):
                    docId_to_url.append(url.strip());
        
        return docId_to_url;
    
    def __generate_data_structures(self):
        self.__generate_docId_to_url();
        self.__generate_webscraping_datastructures();
    
    def __generate_docId_to_url(self):
        docId_to_url = self.__textData.getDocId_to_url();
        self.__read_input_file_helper(docId_to_url); 
        return
    
    def __generate_webscraping_datastructures(self):
        self.__webscraper.scrape_the_web();
        return
    
    def __is_doc_already_scanned(self, url, docId_to_url):
        if url in docId_to_url:
            return True; 
        else:
            return False;