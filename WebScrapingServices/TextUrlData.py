
# contains all the data structures and data access methods
class TextUrlData():
    
    def __init__(self):
        self.__wordId_to_word = [];
        self.__docId_to_url = [];
        self.__words_per_document = [];
        self.__wordId_to_docIds = {};
        self.__word_to_url = {};
    
    def clear_datastructures(self):
        del self.__wordId_to_word[:];
        del self.__docId_to_url[:];
        del self.__words_per_document[:];
        self.__wordId_to_docIds.clear();
        self.__word_to_url.clear();
        
    def getWordId_to_word(self):
        return self.__wordId_to_word; 
    
    def setWordId_to_word(selfs, __wordId_to_word):
        del self.__wordId_to_word[:];
        for word in __wordId_to_word:
            self.__wordId_to_word.append(word);
        
    def getWords_per_document(self):
        return self.__words_per_document;
    
    def setWords_per_document(self, __words_per_document):
        del self.__words_per_document[:];
        for words in __words_per_document:
            self.__words_per_document.append(words);
        
    def getDocId_to_url(self):
        return self.__docId_to_url;
    
    def setDocId_to_url(self, __docId_to_url):
        del self.__docId_to_url[:];
        for url in __docId_to_url:
            self.__docId_to_url.append(url);
        
    def getWordId_to_DocIds(self):
        return self.__wordId_to_docIds;
    
    def setWordId_to_DocIds(self, __wordId_to_docIds):
        self.__wordId_to_docIds.clear();
        for word_id, doc_ids in __wordId_to_docIds.iteritems():
            self.__wordId_to_docIds[word_id] = doc_ids;
    
    def getWord_to_url(self): 
        return self.__word_to_url; 
    
    def setWord_to_url(self, __word_to_url):
        self.__word_to_url.clear();
        for word, urls in __word_to_url.iteritems():
            self.__word_to_url[word] = urls
    