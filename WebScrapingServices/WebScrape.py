from bs4 import BeautifulSoup
import requests as requests
import re

# Beautiful Soup API calls
class WebScrape():
    
    def __init__(self, textData):
        self.__textData = textData;
        self.__docId_to_url = self.__textData.getDocId_to_url();
        self.__words_per_document = self.__textData.getWords_per_document();
        self.__wordId_to_word = self.__textData.getWordId_to_word();
        self.__wordId_to_docIds = self.__textData.getWordId_to_DocIds();
        
    def scrape_the_web(self, url_list):
        
        # load all words of one url into an array (separation by spaces), and is contained in a bigger array indexed by document ids
        for url in url_list:
            array = [];
            array = self.__call_beautiful_soup(url, array);
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
        
        array = self.__parse_soup_text(soup);
        return array;
    
    def __parse_soup_text(self, soup):
        [s.extract() for s in soup(['iframe', 'script', 'meta', 'style'])]
        
        body = soup.find('body');

        list = [];
        for tag in body.findAll():
            
            inner_list = tag.text.split();
            for word in inner_list:
                if word:
                    parsed = word.replace('\n','').replace('\t', '').replace('\r', '').replace(',', '').replace('.', '').strip();
                    list.append(parsed);
        
        return list;
    
    # further polish words, excluding certain characters within words (such as commas, etc.)
    def __cleanup_word(self, old_word):
        new_word = old_word.replace(',', '').replace('.', '').replace('<', '').replace('>', '').replace('?', '');
        return new_word
    
    def __is_valid_word(self, word):
         if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) \
            and ('-' not in word) and ('(' not in word) and (')' not in word) and ('_' not in word) \
            and ('\\' not in word) and ('/' not in word) and ('}' not in word) and ('{' not in word) \
            and ('=' not in word) and ('$' not in word) and ('meta' not in word) \
            and ('charset' not in word) and ('script' not in word) and ('#' not in word) and ('=' not in word) \
            and ('|' not in word):
             return True;
         else:
             return False;
    
    def __parse_document(self, document):
        document = re.sub('<([^>]*)>', '', document.prettify());
        return document;
