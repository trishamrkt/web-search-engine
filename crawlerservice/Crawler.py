class Crawler():

    def __init__(self, textData):
        self.textData = textData;
        self.__docId_to_url = self.textData.getDocId_to_url();
        self.__words_per_document = self.textData.getWords_per_document();
        self.__wordId_to_word = self.textData.getWordId_to_word();
        self.__wordId_to_docIds = self.textData.getWordId_to_DocIds();
        
    def get_resolved_inverted_index(self):
        resolved_inverted_index = {};

        # mapping real words and doc urls with their id's and putting them in a dictionary (as specified for Lab1)
        for word_id, doc_ids in self.__wordId_to_docIds.iteritems():
            word = self.__wordId_to_word[word_id];
            docs = set();
            
            for doc_id in doc_ids:
                docs.add(self.__docId_to_url[doc_id]);
            
            resolved_inverted_index[word] = docs;
        
        return resolved_inverted_index;
