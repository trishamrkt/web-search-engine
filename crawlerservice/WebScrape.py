from bs4 import BeautifulSoup
import requests 

# Beautiful Soup API calls
class WebScrape():
    
    def __init__(self, textData):
        self.textData = textData;
        self.docId_to_url = self.textData.getDocId_to_url();
        self.words_per_document = self.textData.getWords_per_document();
        self.wordId_to_word = self.textData.getWordId_to_word();
        self.wordId_to_docIds = self.textData.getWordId_to_DocIds();
        
    def scrape_the_web(self):
        
        # use beautiful soup to load words of each document into an array of an array, indexed by doc_id
        for url in self.docId_to_url:
            array = []; 
            self.__call_beautiful_soup(url, array);
            self.words_per_document.append(array);
        
        for document in self.words_per_document:
            doc_id = self.words_per_document.index(document); 
            
            for word in document:
                if word not in self.wordId_to_word:
                    self.wordId_to_word.append(word);
                    index = self.wordId_to_word.index(word);
                    
                    self.wordId_to_docIds[index] = [];
                    self.docId_to_url[doc_id]
                    self.wordId_to_docIds[index].append(doc_id);
                    
                else:
                    index = self.wordId_to_word.index(word);
                    
                    if self.words_per_document.index(document) not in self.wordId_to_docIds[index]:
                        self.wordId_to_docIds[index].append(doc_id);   
        return
    
    def __call_beautiful_soup(self, url, array):
        r = requests.get(url)
        data = r.content
        soup = BeautifulSoup(data)

        everything = soup.findAll();       
        list = everything[0].prettify().split(); 
        
        for word in list:
            if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) \
            and ('\"' not in word) and ('-' not in word) and ('(' not in word) and (')' not in word) \
            and ('\\' not in word) and ('/' not in word) and ('}' not in word) and ('{' not in word) \
            and ('=' not in word) and ('$' not in word):
                array.append(self.__clean_up_string(word))
        
        print array;
        return 
    
    def __clean_up_string(self, old_word):
        new_word = old_word.replace(',', '').replace('.', '').replace('<', '').replace('>', '').replace('?', '');
        return new_word
        