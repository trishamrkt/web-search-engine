
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
        db_list = [];
        
        for url in url_list:
            if url not in db_list:
                new_list.append(url);
        
        return url_list
    
    def persist_docId_to_url(self, docId_to_url):
        """
        Persists docId_to_url to DB
        """
        # Get database url list function (docId to url)
        db_list = [];
        
        db_list = db_list + docId_to_url;
        
        # Set database url list function
        
        return
    
    def persist_wordId_to_word(self, wordId_to_word):
        """
        Persists wordId_to_word to DB
        """
        
        
        return
    
    def persist_wordId_to_docId(self, wordId_to_docId):
        """
        Persists wordId_to_docId
        """
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