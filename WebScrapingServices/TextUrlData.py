import pymongo
from pymongo import MongoClient
# contains all the data structures and data access methods
class TextUrlData():

    def __init__(self):
        # Establish MongoDB Connections
        self.client = MongoClient('localhost', 27017)
        self.db = client.GoogaoDB

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
        word self.access_collections("wordId_to_word", "wordId", word_id, "word");
        return word

    # Given doc_id -> return string: url
    def get_url_from_doc_id(self, doc_id):
        url = self.access_collections("docId_to_url", "docId", doc_id, "url")
        return url

    # Given word_id -> return array: doc_ids containing word_id
    def get_doc_ids_from_word_id(self, word_id):
        doc_ids = self.access_collections("wordId_to_docIds", "wordId", word_id, "docIds")
        return doc_ids

    # Given word -> return array: urls containing word
    def get_urls_from_word(self, word):
        urls = self.access_collections("word_to_url", "word", word, "url")
        return urls
