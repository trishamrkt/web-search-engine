from bs4 import BeautifulSoup
import requests as requests

# Beautiful Soup API calls
class WebScrape():
    
    def __init__(self, textData):
        self.__textData = textData;
        self.__docId_to_url = self.__textData.getDocId_to_url();
        self.__words_per_document = self.__textData.getWords_per_document();
        self.__wordId_to_word = self.__textData.getWordId_to_word();
        self.__wordId_to_docIds = self.__textData.getWordId_to_DocIds();
        
    def scrape_the_web(self):
        
        # load all words of one url into an array (separation by spaces), and is contained in a bigger array indexed by document ids
        for url in self.__docId_to_url:
            array = []; 
            self.__call_beautiful_soup(url, array);
            self.__words_per_document.append(array);
        
        # 1. separate words into individual indices, keeping uniqueness
        # 2. putting common words between documents in single pair of a dictionary
        for document in self.__words_per_document:
            doc_id = self.__words_per_document.index(document); 
            
            for word in document:
                
                # 1
                if word not in self.__wordId_to_word:
                    self.__wordId_to_word.append(word);
                    index = self.__wordId_to_word.index(word);
                    
                    # 2
                    self.__wordId_to_docIds[index] = set();
                    self.__wordId_to_docIds[index].add(doc_id);
                    
                else:
                    # 2
                    index = self.__wordId_to_word.index(word);
                    if self.__words_per_document.index(document) not in self.__wordId_to_docIds[index]:
                        self.__wordId_to_docIds[index].add(doc_id);
        
        return
    
    def __call_beautiful_soup(self, url, array):
        r = requests.get(url);
        data = r.content;
        soup = BeautifulSoup(data, 'html.parser');

        everything = soup.findAll();       
        list = everything[0].prettify().split(); 
        
        # exclude words containing the following characters
        for word in list:
            if self.__is_valid_word(word):
                array.append(self.__cleanup_word(word))
        
        return 
    
    # further polish words, excluding certain characters within words (such as commas, etc.)
    def __cleanup_word(self, old_word):
        new_word = old_word.replace(',', '').replace('.', '').replace('<', '').replace('>', '').replace('?', '');
        return new_word
    
    def __is_valid_word(self, word):
         if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) \
            and ('\"' not in word) and ('-' not in word) and ('(' not in word) and (')' not in word) \
            and ('\\' not in word) and ('/' not in word) and ('}' not in word) and ('{' not in word) \
            and ('=' not in word) and ('$' not in word):
             return False;
         else:
             return True;
        