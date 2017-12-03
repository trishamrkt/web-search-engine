import re
from time import clock

class SearchResultsHelper():
    
    def __init__(self):
        pass
    
    def replace(self, word):
        word = re.sub(r'\W+', '' , word);
        return word;
            
    def extract_keywords(self, keywords):
        ka = keywords.split(' ');
        banned_words = ['the', 'in', 'a', 'and', 'to', 'then', 'to', 'is'];
        
        print 'keyword is: ' + keywords;
        
        for word in banned_words:
            self.__remove_word_from_array(word, ka);
        
        print ka;
        return ka;
        
    def lower_case(self, keywords):
        lower_keywords = [];
        
        for word in keywords:
            lower_keywords.append(self.replace(word.lower()));
        
        return lower_keywords;
            
    def __remove_word_from_array(self, word, array):
        while word in array:
            array.remove(word);
    

    