from TextUrlData import *; 
from Crawler import *;
from WebScrape import *;

# this class provides all methods for loading the data structures

class CrawlerService():
    
    def __init__(self, __textUrlData, __pageRankData):
        # instantiates data / service classes
        self.__textData = __textUrlData;
        self.__pageRankData = __pageRankData;
        self.__webscraper = WebScrape(self.__textData, self.__pageRankData);
        self.__crawler = Crawler(self.__textData); 
        
        # loads all data structures by calling lower tier helper classes
        self.__generate_data_structures();
        
    def get_resolved_inverted_index(self): 
        # Include DB access code to return resolved inverted index
        return
    
    def get_inverted_index(self):
        # Include DB access code to return inverted index
        return
    
    # Private Helper Functions
    # Reads input file from base path of application
    def __read_input_file_helper(self, docId_to_url):
        with open('url.txt') as inputfile:
            for url in inputfile:
                if not self.__is_doc_already_scanned(url.strip(), docId_to_url):
                    newurl =url.strip();
                    if newurl:
                        docId_to_url.append(url.strip());
        
        return docId_to_url;
    
    def get_images_from_urls(self, url_list):
        image_urls = [];
        
        for obj in url_list:
            print 'URL is: ' + obj['url'];
            images = self.__textData.get_imageurls_by_url(obj['url']);
            image_urls = image_urls + images;
            
        return image_urls;
    
    def __generate_data_structures(self):
        docId_to_url = self.__generate_docId_to_url();
        self.__generate_webscraping_datastructures(docId_to_url);
    
    def __generate_docId_to_url(self):
        docId_to_url = [];
        self.__read_input_file_helper(docId_to_url); 
        return docId_to_url;
    
    def __generate_webscraping_datastructures(self, docId_to_url):
        self.__webscraper.scrape_the_web(docId_to_url);
        return
    
    def __is_doc_already_scanned(self, url, docId_to_url):
        if url in docId_to_url:
            return True; 
        else:
            return False;