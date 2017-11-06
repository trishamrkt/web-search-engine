import pymongo
from pymongo import MongoClient
# contains all the data structures and data access methods
class TextUrlData():

    def __init__(self):
        # Establish MongoDB Connections
        self.client = MongoClient('localhost', 27017)
        self.db = self.client.GoogaoDB

        self.__wordId_to_word = [];
        self.__docId_to_url = [];
        self.__words_per_document = [];
        self.__wordId_to_docIds = {};
        self.__word_to_url = {};


    """ DATABASE ACCESS FUNCTIONS:
        All follow 3 steps:
        1. Connect to appropriate collection within GoogaoDB
        2. Query collection for desired value (will obtain a dictionary)
        3. Return desired value from dictionary
    """
    def access_collections(self, collection_name, query_key, query_val, desired_key):
        # 1.
        collection = self.db[collection_name]

        # 2. Obtain desired dictionary from collection
        dictionary = collection.find_one({query_key : query_val})

        # 3.
        desired_val = dictionary[desired_key]
        return desired_val

    # Given a word_id  -> return string: word
    def get_word_from_word_id(self, word_id):
        word_dict = self.db["wordId_to_word"].find_one()
        word_array = word_dict['words']
        return word_array[word_id]

    # Given word -> returns int: word_id (if exists) / None (if not)
    def get_word_id_from_word(self, word):
        word_array = self.get_word_array()
        try:
            word_id = word_array.index(word)
            return word_id
        except:
            return None

    # Return all words in all urls
    def get_word_array(self):
        word_dict = self.db["wordId_to_word"].find_one()
        if word_dict != None:
            return word_dict['words']
        else:
            return []

    # Given doc_id -> return string: url
    def get_url_from_doc_id(self, doc_id):
        url_dict = self.db["docId_to_url"].find_one()
        url_array = url_dict['url']
        return url_array[doc_id]

    # Return all urls in url.txt
    def get_url_array(self):
        url_dict = self.db["docId_to_url"].find_one()
        if url_dict != None:
            return url_dict['url']
        else:
            return []

    # Given word_id -> return array: doc_ids containing word_id
    def get_doc_ids_from_word_id(self, word_id):
        word_id_to_doc_ids = self.db["wordId_to_docIds"]
        word_ids = [x['wordId'] for x in word_id_to_doc_ids.find()]
        if word_id in word_ids:
            return self.access_collections("wordId_to_docIds", "wordId", word_id, "docIds")
        else:
            return None

    # Given word -> return array: urls containing word
    def get_urls_from_word(self, word):
        word_to_urls = self.db["word_to_url"]
        words = [x['word'] for x in word_to_urls.find()]
        if word in words:
            return self.access_collections("word_to_url", "word", word, "url")
        else:
            return None
    
    # Given url -> return title of that url 
    def get_title_from_url(self, url):
        url_to_title = self.db["url_to_title"]
        urls = [x['url'] for x in url_to_title.find()]
        if url in urls:
            return self.access_collections("url_to_title", "url", url, "title")
        else:
            return None
    
    # Given url -> return description for that urls's webpage (first sentences in ascii)
    def get_description_from_url(self, url):
        url_to_description = self.db["url_to_description"]
        urls = [x['url'] for x in url_to_description.find()]
        if url in urls:
            return self.access_collections("url_to_description", "url", url, "desc")
        else:
            return None
        
        
    """ DATABASE UPDATE FUNCTIONS:
        All follow 2 steps:
        1. Connect to appropriate collection within GoogaoDB
        2. Set query dictionary to updated value
    """
    def update_collections(self, collection_name, query_key, query_val, update_key, update_val):
        # 1.
        collection = self.db[collection_name]

        # 2.
        collection.update_one({query_key : query_val},  {'$set' : {update_key : update_val}}, upsert=True)

    # Set new url_array (all urls in url.txt)
    def set_url_from_doc_id(self, new_url_array):
        url_array = self.get_url_array()
        self.update_collections("docId_to_url", "url", url_array, "url", new_url_array)

    # Set new word_array (all words in urls)
    def set_word_from_word_id(self, new_word_array):
        word_array = self.get_word_array()
        self.update_collections("wordId_to_word", "words", word_array, "words", new_word_array)

    # Set new doc_ids for a word_id
    def set_doc_ids_from_word_id(self, word_id, new_doc_ids):
        self.update_collections("wordId_to_docIds", "wordId", word_id, "docIds", new_doc_ids)

    # Set urls array for a word
    def set_urls_from_word(self, word, new_urls):
        self.update_collections("word_to_url", "word", word, "url", new_urls)
    
    # Update title for a url
    def update_title_from_url(self, url, title):
        self.update_collections("url_to_title", "url", url, "title", title);
       
    # Update description for a url 
    def update_description_from_url(self, url, description):
        self.update_collections("url_to_description", "url", url, "desc", description);
        
    def close_connection(self):
        self.client.close()
