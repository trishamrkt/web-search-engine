from TextUrlData import *; 
from Crawler import *;
from WebScrape import *;

# this class provides all methods for loading the data structures

class CrawlerService():
    
    def __init__(self):
        self.textData = TextUrlData();
        self.webscraper = WebScrape(self.textData);
        self.crawler = Crawler(self.textData); 
        
        self.generate_docId_to_url();
        self.webscraper.scrape_the_web();
        self.get_resolved_inverted_index();
    
    def generate_docId_to_url(self):
        docId_to_url = self.textData.getDocId_to_url();
        self.__read_input_file_helper(docId_to_url); 
        
        return
    
    def get_resolved_inverted_index(self): 
#         print self.crawler.get_resolved_inverted_index();
        
        return
        
    # Private Helper Functions
    
    # Reads input file from base path of application
    # @Return     
    def __read_input_file_helper(self, docId_to_url):
        with open('input.txt') as inputfile:
            for line in inputfile:
                docId_to_url.append(line.strip());
        return docId_to_url;
    
    