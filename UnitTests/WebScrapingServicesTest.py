import unittest
import numpy as np
from WebScrapingServices.Crawler import *
from WebScrapingServices.WebScrape import *
from WebScrapingServices.TextUrlData import *

class WebScrapingServicesTest(unittest.TestCase):
    
    # For each new test, the data structures are refreshed, and the API is called again using a different URL
    def setUp(self):
        self.__textData = TextUrlData();
        self.__webScraper = WebScrape(self.__textData);
        self.__crawler = Crawler(self.__textData);
     
    # Match each word of the computed result set with the expected result set
    def test_wordId_to_wordid_advanced(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __wordId_to_word = self.__textData.getWordId_to_word();
        isValid = False; 
        
        resultSet = ['Hi', 'thereee', 'In', 'the', 'Olympian', 'creation', 'myth', 'as', 'Hesiod', 'tells', 'it', 'in', 'Theogony', 'Uranus', 'came', \
                     'every', 'night', 'to', 'cover', 'earth', 'and', 'mate', 'with', 'Gaia', 'but', 'he', 'hated', 'children', 'she', 'bore', 'him', \
                     'named', 'their', 'first', 'six', 'sons', 'daughters', 'Titans', 'three', 'one-hundred-handed', 'giants', 'Hekatonkheires', \
                     'one-eyed', 'Cyclopes', 'imprisoned', "Gaia's", 'youngest', 'Tartarus', 'deep', 'within', 'Earth', 'where', 'they', 'caused', \
                     'pain', 'She', 'shaped', 'a', 'great', 'flint-bladed', 'sickle', 'asked', 'her', 'castrate', 'Only', 'Cronus', 'most', 'ambitious', \
                     'of', 'was', 'willing:', 'ambushed', 'his', 'father', 'castrated', 'casting', 'severed', 'testicles', 'into', 'sea', 'For', 'this', \
                     'fearful', 'deed', 'called', 'Titanes', 'Theoi', 'or', '"Straining', 'Gods"', 'From', 'blood', 'that', 'spilled', 'from', 'onto', \
                     'forth', 'Giants', 'Erinyes', '(the', 'avenging', 'Furies)', 'Meliae', 'ash-tree', 'nymphs)', 'according', 'some', 'Telchines', 'genitals', \
                     'Aphrodite', 'The', 'learned', 'Alexandrian', 'poet', 'Callimachus', 'reported', 'bloodied', 'had', 'been', 'buried', 'at', 'Zancle', \
                     'Sicily', 'Romanized', 'Greek', 'traveller', 'Pausanias', 'informed', 'thrown', 'cape', 'near', 'Bolina', 'not', 'far', 'Argyra', 'on', \
                     'coast', 'Achaea', 'whereas', 'historian', 'Timaeus', 'located', 'Corcyra;', 'Corcyrans', 'claimed', 'be', 'descendants', 'wholly', \
                     'legendary', 'Phaeacia', 'visited', 'by', 'Odysseus', 'circa', '500', 'BCE', 'one', 'mythographer', 'Acusilaus', 'claiming', 'Phaeacians', \
                     'sprung', 'very', "Uranus'", 'castration', 'After', 'deposed', 're-imprisoned', 'then', 'prophesied', 'turn', 'destined', 'overthrown', \
                     'own', 'son', 'so', 'Titan', 'attempted', 'avoid', 'fate', 'devouring', 'young', 'Zeus', 'through', 'deception', 'mother', 'Rhea', 'avoided', \
                     'These', 'ancient', 'myths', 'distant', 'origins', 'were', 'expressed', 'cults', 'among', 'Hellenes', 'function', 'vanquished', 'god', 'an', \
                     'elder', 'time', 'before', 'real', 'began'];
        
        isValid = np.array_equal(np.array(resultSet), np.array(__wordId_to_word))
        self.assertEqual(isValid, True, 'Mismatch between expected and actual result sets for: WordId to Word mapping');
        
        return
    
    # Calls WebScraper's scraping API, evaluates whether the returned datastructure is as expected
    def test_wordId_to_word_intermediate(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest2']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __wordId_to_word = self.__textData.getWordId_to_word();
        isValid = False;
        
        resultSet = ['Hi', 'thereee', 'Company', 'Contact', 'Country', 'Alfreds', 'Futterkiste', 'Maria', 'Anders', 'Germany', 'Centro', 'comercial', 'Moctezuma', \
                     'Francisco', 'Chang', 'Mexico', 'Ernst', 'Handel', 'Roland', 'Mendel', 'Austria', 'Island', 'Trading', 'Helen', 'Bennett', 'UK', 'Laughing', \
                     'Bacchus', 'Winecellars', 'Yoshi', 'Tannamuri', 'Canada', 'Magazzini', 'Alimentari', 'Riuniti', 'Giovanni', 'Rovelli', 'Italy', 'Coffee', 'Tea',\
                      'Milk', 'An', 'Ordered', 'HTML', 'List']

        isValid = np.array_equal(np.array(resultSet), np.array(__wordId_to_word));
        self.assertEqual(isValid, True, 'Mismatch between expected and actual result sets for: WordId to Word mapping');

    # Calls WebScraper's scraping API, evaluates whether the returned datastructure is as expected
    def test_wordId_to_docIds_advanced(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __wordId_to_docIds = self.__textData.getWordId_to_DocIds(); 
        isValid = False;
        
        resultSet = {0: set([0]), 1: set([0]), 2: set([0]), 3: set([0]), 4: set([0]), 5: set([0]), 6: set([0]), 7: set([0]), 8: set([0]), 9: set([0]), \
                     10: set([0]), 11: set([0]), 12: set([0]), 13: set([0]), 14: set([0]), 15: set([0]), 16: set([0]), 17: set([0]), 18: set([0]), \
                     19: set([0]), 20: set([0]), 21: set([0]), 22: set([0]), 23: set([0]), 24: set([0]), 25: set([0]), 26: set([0]), 27: set([0]), \
                     28: set([0]), 29: set([0]), 30: set([0]), 31: set([0]), 32: set([0]), 33: set([0]), 34: set([0]), 35: set([0]), 36: set([0]), \
                     37: set([0]), 38: set([0]), 39: set([0]), 40: set([0]), 41: set([0]), 42: set([0]), 43: set([0]), 44: set([0]), 45: set([0]), \
                     46: set([0]), 47: set([0]), 48: set([0]), 49: set([0]), 50: set([0]), 51: set([0]), 52: set([0]), 53: set([0]), 54: set([0]), \
                     55: set([0]), 56: set([0]), 57: set([0]), 58: set([0]), 59: set([0]), 60: set([0]), 61: set([0]), 62: set([0]), 63: set([0]), \
                     64: set([0]), 65: set([0]), 66: set([0]), 67: set([0]), 68: set([0]), 69: set([0]), 70: set([0]), 71: set([0]), 72: set([0]), \
                     73: set([0]), 74: set([0]), 75: set([0]), 76: set([0]), 77: set([0]), 78: set([0]), 79: set([0]), 80: set([0]), 81: set([0]), \
                     82: set([0]), 83: set([0]), 84: set([0]), 85: set([0]), 86: set([0]), 87: set([0]), 88: set([0]), 89: set([0]), 90: set([0]), \
                     91: set([0]), 92: set([0]), 93: set([0]), 94: set([0]), 95: set([0]), 96: set([0]), 97: set([0]), 98: set([0]), 99: set([0]), \
                     100: set([0]), 101: set([0]), 102: set([0]), 103: set([0]), 104: set([0]), 105: set([0]), 106: set([0]), 107: set([0]), 108: set([0]), \
                     109: set([0]), 110: set([0]), 111: set([0]), 112: set([0]), 113: set([0]), 114: set([0]), 115: set([0]), 116: set([0]), 117: set([0]), \
                     118: set([0]), 119: set([0]), 120: set([0]), 121: set([0]), 122: set([0]), 123: set([0]), 124: set([0]), 125: set([0]), 126: set([0]), \
                     127: set([0]), 128: set([0]), 129: set([0]), 130: set([0]), 131: set([0]), 132: set([0]), 133: set([0]), 134: set([0]), 135: set([0]), \
                     136: set([0]), 137: set([0]), 138: set([0]), 139: set([0]), 140: set([0]), 141: set([0]), 142: set([0]), 143: set([0]), 144: set([0]), \
                     145: set([0]), 146: set([0]), 147: set([0]), 148: set([0]), 149: set([0]), 150: set([0]), 151: set([0]), 152: set([0]), 153: set([0]), \
                     154: set([0]), 155: set([0]), 156: set([0]), 157: set([0]), 158: set([0]), 159: set([0]), 160: set([0]), 161: set([0]), 162: set([0]), \
                     163: set([0]), 164: set([0]), 165: set([0]), 166: set([0]), 167: set([0]), 168: set([0]), 169: set([0]), 170: set([0]), 171: set([0]), \
                     172: set([0]), 173: set([0]), 174: set([0]), 175: set([0]), 176: set([0]), 177: set([0]), 178: set([0]), 179: set([0]), 180: set([0]), \
                     181: set([0]), 182: set([0]), 183: set([0]), 184: set([0]), 185: set([0]), 186: set([0]), 187: set([0]), 188: set([0]), 189: set([0]), \
                     190: set([0]), 191: set([0]), 192: set([0]), 193: set([0]), 194: set([0]), 195: set([0]), 196: set([0]), 197: set([0]), 198: set([0]), \
                     199: set([0]), 200: set([0]), 201: set([0]), 202: set([0]), 203: set([0]), 204: set([0]), 205: set([0]), 206: set([0])};
        
        isValid = self.__is_dictionaries_same(resultSet, __wordId_to_docIds)
        self.assertEqual(isValid, True, '[ADVANCED] Mismatch between expected and actual result sets for: WordId to DocIds mapping');

        return 

    # Calls WebScraper's scraping API, evaluates whether the returned datastructure is as expected
    def test_wordId_to_docIds_intermediate(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest2']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __wordId_to_docIds = self.__textData.getWordId_to_DocIds();
        isValid = False;
        
        resultSet = {0: set([0]), 1: set([0]), 2: set([0]), 3: set([0]), 4: set([0]), 5: set([0]), 6: set([0]), 7: set([0]), 8: set([0]), 9: set([0]), \
                     10: set([0]), 11: set([0]), 12: set([0]), 13: set([0]), 14: set([0]), 15: set([0]), 16: set([0]), 17: set([0]), 18: set([0]), \
                     19: set([0]), 20: set([0]), 21: set([0]), 22: set([0]), 23: set([0]), 24: set([0]), 25: set([0]), 26: set([0]), 27: set([0]), \
                     28: set([0]), 29: set([0]), 30: set([0]), 31: set([0]), 32: set([0]), 33: set([0]), 34: set([0]), 35: set([0]), 36: set([0]), \
                     37: set([0]), 38: set([0]), 39: set([0]), 40: set([0]), 41: set([0]), 42: set([0]), 43: set([0]), 44: set([0])};
        
        isValid = self.__is_dictionaries_same(resultSet, __wordId_to_docIds)
        self.assertEqual(isValid, True, '[INTERMEDIATE]: Mismatch between expected and actual result sets for: WordId to DocIds mapping');

        return 
    
     # Calls WebScraper's scraping API, evaluates whether the returned datastructure is as expected
    def test_word_to_url_advanced(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __word_to_url = self.__textData.getWord_to_url();
        isValid = False;
        str_replace = 'http://localhost:8000/lab1unittest';

        resultSet = {'Tartarus': set([str_replace]), 'six': set([str_replace]), 'legendary': set([str_replace]), 'traveller': set([str_replace]), 'caused': set([str_replace]), \
                     'sickle': set([str_replace]), 'through': set([str_replace]), 'expressed': set([str_replace]), 'Bolina': set([str_replace]), 'earth': set([str_replace]), \
                     'children': set([str_replace]), 'before': set([str_replace]), 'testicles': set([str_replace]), 'hated': set([str_replace]), 'father': set([str_replace]), \
                     'young': set([str_replace]), 'to': set([str_replace]), 'Hi': set([str_replace]), 'Zancle': set([str_replace]), 'ash-tree': set([str_replace]), \
                     'Hellenes': set([str_replace]), 'giants': set([str_replace]), 'then': set([str_replace]), 'his': set([str_replace]), 'casting': set([str_replace]), \
                     'myth': set([str_replace]), 'descendants': set([str_replace]), 'far': set([str_replace]), 'Achaea': set([str_replace]), 'Cronus': set([str_replace]), \
                     'Meliae': set([str_replace]), 'sons': set([str_replace]), 'every': set([str_replace]), 'She': set([str_replace]), 'they': set([str_replace]), \
                     'not': set([str_replace]), 'cape': set([str_replace]), 'one': set([str_replace]), 'him': set([str_replace]), 'overthrown': set([str_replace]), \
                     'Hesiod': set([str_replace]), 'imprisoned': set([str_replace]), 'shaped': set([str_replace]), 'thereee': set([str_replace]), 'Romanized': set([str_replace]), \
                     'this': set([str_replace]), 'castration': set([str_replace]), 'she': set([str_replace]), 'Uranus': set([str_replace]), 'night': set([str_replace]), \
                     'distant': set([str_replace]), 'severed': set([str_replace]), 'where': set([str_replace]), '"Straining': set([str_replace]), 'Sicily': set([str_replace]), \
                     'From': set([str_replace]), '(the': set([str_replace]), 'For': set([str_replace]), 'willing:': set([str_replace]), 'creation': set([str_replace]), \
                     'flint-bladed': set([str_replace]), 'Only': set([str_replace]), 'Olympian': set([str_replace]), 'sea': set([str_replace]), 'Rhea': set([str_replace]), \
                     'bore': set([str_replace]), 'avoided': set([str_replace]), 'Giants': set([str_replace]), 'and': set([str_replace]), 'one-eyed': set([str_replace]), \
                     'god': set([str_replace]), 'avoid': set([str_replace]), 'Zeus': set([str_replace]), 'Furies)': set([str_replace]), 'wholly': set([str_replace]), \
                     'Argyra': set([str_replace]), 'mate': set([str_replace]), 'Titanes': set([str_replace]), 'learned': set([str_replace]), 'forth': set([str_replace]), \
                     'castrate': set([str_replace]), 'be': set([str_replace]), 'Hekatonkheires': set([str_replace]), 'Corcyra;': set([str_replace]), 'deposed': set([str_replace]), \
                     'sprung': set([str_replace]), 'youngest': set([str_replace]), 'reported': set([str_replace]), 'from': set([str_replace]), 'by': set([str_replace]), \
                     'thrown': set([str_replace]), 'avenging': set([str_replace]), 'great': set([str_replace]), 'her': set([str_replace]), 'origins': set([str_replace]), \
                     'Greek': set([str_replace]), 'of': set([str_replace]), 'spilled': set([str_replace]), 'Corcyrans': set([str_replace]), 'according': set([str_replace]), \
                     'turn': set([str_replace]), 'onto': set([str_replace]), 'asked': set([str_replace]), 'first': set([str_replace]), 'among': set([str_replace]), \
                     'named': set([str_replace]), 'own': set([str_replace]), 'Telchines': set([str_replace]), 'ambushed': set([str_replace]), 'BCE': set([str_replace]), \
                     'into': set([str_replace]), 'within': set([str_replace]), 'son': set([str_replace]), 'elder': set([str_replace]), 'Alexandrian': set([str_replace]), \
                     'on': set([str_replace]), 'ancient': set([str_replace]), 'deception': set([str_replace]), 'bloodied': set([str_replace]), 'Erinyes': set([str_replace]), \
                     'informed': set([str_replace]), 'Callimachus': set([str_replace]), 'been': set([str_replace]), 'myths': set([str_replace]), 'their': set([str_replace]), \
                     'poet': set([str_replace]), 'circa': set([str_replace]), 'was': set([str_replace]), 'Theogony': set([str_replace]), '500': set([str_replace]), \
                     'function': set([str_replace]), 'one-hundred-handed': set([str_replace]), 'Timaeus': set([str_replace]), 'that': set([str_replace]), 'These': set([str_replace]), \
                     'some': set([str_replace]), 'Phaeacians': set([str_replace]), 'but': set([str_replace]), 'historian': set([str_replace]), 'with': set([str_replace]), \
                     'he': set([str_replace]), 'genitals': set([str_replace]), "Gaia's": set([str_replace]), 'Acusilaus': set([str_replace]), 'fearful': set([str_replace]), \
                     'Titan': set([str_replace]), "Uranus'": set([str_replace]), 'near': set([str_replace]), 'Cyclopes': set([str_replace]), 'three': set([str_replace]), \
                     'were': set([str_replace]), 'visited': set([str_replace]), 'called': set([str_replace]), 'buried': set([str_replace]), 'Theoi': set([str_replace]), \
                     'real': set([str_replace]), 'Odysseus': set([str_replace]), 'castrated': set([str_replace]), 'mythographer': set([str_replace]), 'nymphs)': set([str_replace]), \
                     'Pausanias': set([str_replace]), 'it': set([str_replace]), 'deep': set([str_replace]), 'an': set([str_replace]), 'as': set([str_replace]), 'at': set([str_replace]), \
                     'in': set([str_replace]), 'claimed': set([str_replace]), 'deed': set([str_replace]), 'devouring': set([str_replace]), 'tells': set([str_replace]), \
                     'Gods"': set([str_replace]), 'fate': set([str_replace]), 'whereas': set([str_replace]), 'After': set([str_replace]), 'claiming': set([str_replace]), \
                     'vanquished': set([str_replace]), 'located': set([str_replace]), 'ambitious': set([str_replace]), 'attempted': set([str_replace]), 'Phaeacia': set([str_replace]), \
                     'Gaia': set([str_replace]), 'daughters': set([str_replace]), 'Titans': set([str_replace]), 'Aphrodite': set([str_replace]), 'pain': set([str_replace]), \
                     'mother': set([str_replace]), 'most': set([str_replace]), 'blood': set([str_replace]), 'destined': set([str_replace]), 'prophesied': set([str_replace]), \
                     'The': set([str_replace]), 'coast': set([str_replace]), 'had': set([str_replace]), 'a': set([str_replace]), 'cults': set([str_replace]), 're-imprisoned': set([str_replace]), \
                     'cover': set([str_replace]), 'or': set([str_replace]), 'so': set([str_replace]), 'time': set([str_replace]), 'very': set([str_replace]), 'Earth': set([str_replace]), \
                     'the': set([str_replace]), 'began': set([str_replace]), 'came': set([str_replace]), 'In': set([str_replace])};
                             
        isValid = self.__is_dictionaries_same(resultSet, __word_to_url);               
        self.assertEqual(isValid, True, '[ADVANCED]: Mismatch between expected and actual result sets for: __word_to_url mapping');
        
        return
    
    # Calls WebScraper's scraping API, evaluates whether the returned datastructure is as expected
    def test_word_to_url_intermediate(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest2']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
        
        __word_to_url = self.__textData.getWord_to_url();
        isValid = False;
        str_replace = 'http://localhost:8000/lab1unittest2';
        
        resultSet = {'Canada': set([str_replace]), 'Futterkiste': set([str_replace]), 'Italy': set([str_replace]), \
                     'Handel': set([str_replace]), 'Rovelli': set([str_replace]), 'Roland': set([str_replace]), \
                     'Alfreds': set([str_replace]), 'thereee': set([str_replace]), 'Coffee': set([str_replace]), \
                     'Francisco': set([str_replace]), 'Giovanni': set([str_replace]), 'Company': set([str_replace]), \
                     'Centro': set([str_replace]), 'HTML': set([str_replace]), 'Germany': set([str_replace]), \
                     'Hi': set([str_replace]), 'Winecellars': set([str_replace]), 'Country': set([str_replace]), \
                     'Mendel': set([str_replace]), 'Moctezuma': set([str_replace]), 'Maria': set([str_replace]), \
                     'comercial': set([str_replace]), 'UK': set([str_replace]), 'Bacchus': set([str_replace]), \
                     'Island': set([str_replace]), 'Helen': set([str_replace]), 'List': set([str_replace]), \
                     'Magazzini': set([str_replace]), 'Contact': set([str_replace]), 'Laughing': set([str_replace]), \
                     'Ernst': set([str_replace]), 'Chang': set([str_replace]), 'Ordered': set([str_replace]), \
                     'Mexico': set([str_replace]), 'Tea': set([str_replace]), 'Bennett': set([str_replace]), \
                     'An': set([str_replace]), 'Alimentari': set([str_replace]), 'Riuniti': set([str_replace]), \
                     'Austria': set([str_replace]), 'Yoshi': set([str_replace]), 'Trading': set([str_replace]), \
                     'Tannamuri': set([str_replace]), 'Anders': set([str_replace]), 'Milk': set([str_replace])};
                             
        isValid = self.__is_dictionaries_same(resultSet, __word_to_url)
        self.assertEqual(isValid, True, '[INTERMEDIATE]: Mismatch between expected and actual result sets for: __word_to_url mapping');
        
        return
    
    # Deletes an index in an array, checks if the value of that index is still inside array, if yes, it means
    # array does not contain unique values
    def test_word_uniqueness_advanced(self):
        self.__textData.clear_datastructures();
        self.__textData.setDocId_to_url(['http://localhost:8000/lab1unittest']);
        self.__webScraper.scrape_the_web(self.__textData.getDocId_to_url());
        self.__textData.setWord_to_url(self.__crawler.get_resolved_inverted_index());
         
        __wordId_to_word = self.__textData.getWordId_to_word(); 
        isValid = True;
        
        for word in __wordId_to_word:
            index = __wordId_to_word.index(word);
            del __wordId_to_word[index]; 
            if word in __wordId_to_word:
                isValid = False;
                break;
        
        self.assertEqual(isValid, True, 'Duplicate word found in WordId_to_Word datastructure');
        return
    
    def __is_dictionaries_same(self, dict1, dict2):
        return dict1 == dict2;
    
if __name__ == '__main__':
    unittest.main();

