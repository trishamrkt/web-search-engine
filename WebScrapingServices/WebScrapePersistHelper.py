
class WebScrapePersistHelper():
    
    def __init__(self, textData, pageRankData):
        self.__textData = textData;
        self.__pageRankData = pageRankData;
        
    def getOutbound(self):
        """
        Returns outbound data structure in database
        """
        return {};
        
    def parse_url(self, url_list):
        """
        Checks with database to narrow the url_list to only URLs not in database
        already
        """
        new_list = [];
        
        # Get database url list (docId to url)
        db_list = self.__textData.get_url_array();
        
        for url in url_list:
            if url not in db_list:
                new_list.append(url);
        
        return url_list
    
    def persist_docId_to_url(self, docId_to_url):
        """
        Persists docId_to_url to DB
        """
        # Get database url list function (docId to url)
        db_list = self.__textData.get_url_array();
        db_list = db_list + docId_to_url;
        
        # Set database url list function
        self.__textData.set_url_from_doc_id(db_list);
        
        return
    
    def persist_wordId_to_word(self, wordId_to_word):
        """
        Persists wordId_to_word to DB
        1. iterate through dictionary
        """
        # Get wordId_to_word from db accessor
        db_wordId_to_word = self.__textData.get_word_array();
        persist = False;
        
        # Iterate through new words
        for word in wordId_to_word:
            
            # If this word does not already exist in db, insert it
            if word not in db_wordId_to_word:
                persist = True;
                db_wordId_to_word.append(word);
        
        # Persist db_wordId_to_word
        if persist:
            self.__textData.set_word_from_word_id(db_wordId_to_word);
        
        return
    
    def persist_wordId_to_docIds(self, wordId_to_docIds, wordId_to_word):
        """
        Persists wordId_to_docId
        """
        # Get wordId_to_word from db accessor
        db_wordId_to_word = [];
        
        for wordId, docIds in wordId_to_docIds.iteritems():
            # Check if this word already exists in DB
            if wordId_to_word[wordId]:
                word = wordId_to_word[wordId];
                
                # Get id of this word (db_wordId_to_word)
                id = self.__textData.get_word_id_from_word(word);
                array = self.__textData.get_doc_ids_from_word_id(id)
                
                if array:
                    # Append to the docIds array
                    for docId in docIds:
                        array.append(docId);
                    # Set that wordId's value to array
                else:
                    # Insert new document with wordId as key and docIds as value
                    
                                    
            
        return
    
    def persist_word_to_url(self, word_to_url):
        """
        Persists word_to_url
        """
        return
    
    def persist_inbound(self, inbound):
        """
        Persists inbound (old + new urls together)
        """
        return
    
    def persist_outbound(self, outbound):
        """
        Persists outbound
        """
        return
    
    def persist_num_links(self, num_links):
        """
        Persists num_links
        """
        return