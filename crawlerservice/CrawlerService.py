from TextUrlData import *; 
from Crawler import *;
from WebScrape import *;

# this class provides all methods for loading the data structures

class CrawlerService():
    
    def __init__(self):
        self.textData = TextUrlData();
        self.crawler = Crawler(); 
        self.webscraper = WebScrape(self.textData);
        
        self.generate_docId_to_url();
        self.generate_word_to_url();
        self.generate_wordId_to_docIds();
        self.generate_wordId_to_word();
        
        self.webscraper.scrape_the_web();
        
        
    def generate_wordId_to_word(self):
        wordId_to_word = self.textData.getWordId_to_Word();
        
        return
    
    def generate_docId_to_url(self):
        docId_to_url = self.textData.getDocId_to_url();
        self.__read_input_file_helper(docId_to_url); 
        
        # Testing function
        print self.textData.docId_to_url
        
        return
    
    def generate_wordId_to_docIds(self):
        
        return 
    
    def generate_word_to_url(self):
        
        return
    
    
    # Private Helper Functions
    
    # Reads input file from base path of application
    # @Return     
    def __read_input_file_helper(self, docId_to_url):
        with open('input.txt') as inputfile:
            for line in inputfile:
                docId_to_url.append(line.strip());
        return docId_to_url;
    
    