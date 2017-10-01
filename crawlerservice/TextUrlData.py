
# contains all the data structures and data access methods
class TextUrlData():
    
    def __init__(self): 
        self.wordId_to_word = []; 
        self.docId_to_url = []; 
        self.words_per_document = [];
        self.wordId_to_docIds = {};
        self.word_to_url = {}; 
    
    def getWordId_to_Word(self):
        return self.getWordId_to_Word; 
    
    def getWords_per_document(self):
        return self.words_per_document;
    
    def getDocId_to_url(self):
        return self.docId_to_url; 
    
    def getWordId_to_DocIds(self): 
        return self.wordId_to_docIds; 
    
    def getWord_to_url(self): 
        return self.word_to_url; 
    