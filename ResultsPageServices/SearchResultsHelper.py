
class SearchResultsHelper():
    
    def __init__(self):
        pass
    
    def extract_keywords(self, keywords):
        ka = keywords.split(' ');
        banned_words = ['the', 'in', 'a', 'and', 'to', 'then', 'to', 'is'];
        
        for word in banned_words:
            self.__remove_word_from_array(word, ka);
        
        return ka;
        
    def __remove_word_from_array(self, word, array):
        while word in array:
            array.remove(word);
    

    