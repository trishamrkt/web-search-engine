
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
        
        # Iterate through new words
        for word in wordId_to_word:
            
            # If this word does not already exist in db, insert it
            if word not in db_wordId_to_word:
                db_wordId_to_word.append(word);
        
        # Persist db_wordId_to_word
        self.__textData.set_word_from_word_id(db_wordId_to_word);
        
        return
    
    def persist_wordId_to_docIds(self, wordId_to_docIds, wordId_to_word):
        """
        Persists wordId_to_docId
        """
        # Get wordId_to_word from db accessor
        db_wordId_to_word = self.__textData.get_word_array();
        
        for wordId, docIds in wordId_to_docIds.iteritems():
            docIds = list(docIds);
            
            # Check if this word already exists in DB
            if wordId_to_word[wordId]:
                word = wordId_to_word[wordId];
                id = self.__textData.get_word_id_from_word(word);
                
                docId_array = self.__textData.get_doc_ids_from_word_id(id)
                
                if docId_array:
                    # Append to the docIds array
                    for docId in docIds:
                        if docId not in docId_array:
                            docId_array.append(docId);
                else:
                    docId_array = docIds;
                    
                # Function takes care of both cases when docId exists and does not exist
                self.__textData.set_doc_ids_from_word_id(id, docId_array);

        return
    
    def persist_word_to_url(self, word_to_url):
        """
        Persists word_to_url
        """
        # Get wordId_to_word from db accessor
        db_wordId_to_word = self.__textData.get_word_array();
        
        for word, url_list in word_to_url.iteritems():
            # Check if word exists in db
            url_array = self.__textData.get_urls_from_word(word);
            
            if url_array:
                for url in url_list:
                    if url not in url_array:
                        url_array.append(url);
            else:
                url_array = list(url_list);
                
            self.__textData.set_urls_from_word(word, url_array);
            
        return
    
    def persist_inbound(self, inbound):
        """
        Persists inbound (old + new urls together)
        """     
        for url, inbound_array in inbound.iteritems():
            self.__pageRankData.update_inbound(url, inbound_array);
            
        return
    
    def persist_outbound(self, outbound):
        """
        Persists outbound
        """
        for url, outbound_array in outbound.iteritems():
            self.__pageRankData.update_outbound(url, outbound_array);
            
        return
    
    def persist_num_links(self, num_links):
        """
        Persists num_links
        """
        for url, num in num_links.iteritems():
            self.__pageRankData.update_num_links(url, num);
            
        return