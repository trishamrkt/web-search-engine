from bs4 import BeautifulSoup
import requests 

# Beautiful Soup API calls
class WebScrape():
    
    def __init__(self, textData):
        self.textData = textData;
        self.docId_to_url = self.textData.getDocId_to_url();
        self.words_per_document = self.textData.getWords_per_document();
        
    def scrape_the_web(self):
        
        # get all words from docId
        for url in self.docId_to_url:
            array = []; 
            self.__call_beautiful_soup(url, array);
            self.words_per_document.append(array);
        return 
    
    def __call_beautiful_soup(self, url, array):
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data)

        everything = soup.findAll();       
        list = everything[0].prettify().split(); 
        
        for word in list:
            if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) and ('\"' not in word) and ('-' not in word) and ('(' not in word) and (')' not in word) and ('}' not in word) and ('{' not in word) and ('=' not in word):
                array.append(word)
        
        return 