
# contains all the data structures and data access methods
class TextUrlData():
    
    def __init__(self): 
        self.__wordId_to_word = []; 
        self.__docId_to_url = []; 
        self.__words_per_document = [];
        self.__wordId_to_docIds = {};
        self.__word_to_url = {};
    
    def getWordId_to_word(self):
        return self.__wordId_to_word; 
    
    def getWords_per_document(self):
        return self.__words_per_document;
    
    def getDocId_to_url(self):
        return self.__docId_to_url;
    
    def getWordId_to_DocIds(self): 
        return self.__wordId_to_docIds; 
    
    def getWord_to_url(self): 
        return self.__word_to_url; 
    