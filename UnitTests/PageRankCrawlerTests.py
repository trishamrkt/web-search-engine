import unittest
import pprint
from WebScrapingServices.TextUrlData import TextUrlData
from PageRankServices.PageRankData import PageRankData
from ResultsPageServices.SearchResultsService import SearchResultsService

class PageRankCrawlerTests(unittest.TestCase):

    def setUp(self):
        self.__textData = TextUrlData();
        self.__pageRankData = PageRankData();
        self.__searchResultsService = SearchResultsService(self.__textData, self.__pageRankData);

    def test_search_word_one(self):
        # Search 'the'
        resultSet = self.__get_result_set(1);
        result = self.__searchResultsService.find_word('adsflkjadscoiualewkrjlakjdociualkjdswer');
        isValid = self.__is_dictionaries_same(resultSet, result);

        self.assertEqual(isValid, True, "Search word 'adsflkjadscoiualewkrjlakjdociualkjdswer' does not match expected output");

        return

    def test_search_word_two(self):
        # Search 'contributions'
        resultSet = self.__get_result_set(2);
        result = self.__searchResultsService.find_word('contributions');
        isValid = self.__is_dictionaries_same(resultSet, result);

        self.assertEqual(isValid, True, str(result));
        pprint.pprint(sorted(self.__pageRankData.get_all_page_ranks().iteritems(), key=lambda (k,v): (v,k), reverse=True));

        return

    def __get_result_set(self, num):
        resultSetOne = {};

        resultSetTwo = {0: {'description': u' 5,505,967 articles in English Arts Biography Geography History Mathematics Science Society Technology All portals From today\'s featured article Wheeled toy animal Rotating locomotion in living...',
                             'url': u'https://en.wikipedia.org/wiki/Main_Page'},
                         1: {'description': u' He rose to fame in October 2012 when he was featured on Disclosure\'s breakthrough single "Latch", which peaked at number eleven on the UK Singles...',
                             'title': u'Sam Smith (singer) - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/Sam_Smith_(singer)'},
                         2: {'description': u' NY 373 is the only connector between US 9 and the hamlet of Port Kent and the ferry that serves it. The hamlet of Port...',
                             'title': u'New York State Route 373 - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/New_York_State_Route_373'},
                         3: {'description': u' Over 130 public transit operators, serving over 5.2 million passengers each day. Twelve major public and private ports, handling more than 110 million short tons...',
                             'title': u'New York State Department of Transportation - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/New_York_State_Department_of_Transportation'},
                         4: {'description': u' The village is named after the Keese family, early settlers from Vermont. It developed along the Ausable River, which provided water power for mills and...',
                             'title': u'Keeseville, New York - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/Keeseville,_New_York'},
                         5: {'description': u" For instance, the only albums that went platinum in the United States in 2014 were the Frozen soundtrack and Taylor Swift's 1989, whereas several artists...",
                             'title': u'Album-equivalent unit - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/Album-equivalent_unit'},
                         6: {'description': u' CDPs are populated areas that generally include one officially designated but currently unincorporated small community, for which the CDP is named, plus surrounding inhabited countryside...',
                             'title': u'Census-designated place - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/Census-designated_place'},
                         7: {'description': u' It contains the advice or opinions of one or more Wikipedia contributors. This page is not one of Wikipedia policies or guidelines, as it has...',
                             'title': u'Wikipedia:Very short featured articles - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/Wikipedia:Very_short_featured_articles'},
                         8: {'description': u" Marys is a Roman Catholic secondary school and sixth form located in Bishop's Stortford, Hertfordshire, England. Contents 1 History 2 Present day 3 Alumni 4...",
                             'title': u"St Mary's Catholic School, Bishop's Stortford - Wikipedia",
                             'url': u'https://en.wikipedia.org/wiki/St_Mary%27s_Catholic_School,_Bishop%27s_Stortford'},
                         9: {'description': u' "Wrote My Way Out" is in the NBA 2K18 soundtrack. Contents 1 Background 2 Commercial performance 3 Track listing 3.1 Notes 4 Charts 5 Awards...',
                             'title': u'The Hamilton Mixtape - Wikipedia',
                             'url': u'https://en.wikipedia.org/wiki/The_Hamilton_Mixtape'}}

        if num == 1:
            return resultSetOne;
        elif num == 2:
            return resultSetTwo;
        else:
            return {};

    def __is_dictionaries_same(self, dict1, dict2):
        for key, url_obj in dict1.iteritems():
            if url_obj['url'] != dict2[key]['url']:
                return False
        return True;

if __name__ == "__main__":
    unittest.main();
