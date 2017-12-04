import pprint
import math
import json
from time import clock

class SearchResultsService():

    def __init__(self, textData, pageRankData, searchResultsHelper):
        self.__textData = textData;
        self.__pageRankData = pageRankData;
        self.__searchResultsHelper = searchResultsHelper;

    def find_word(self, keyword):
        """
        4 Steps to finding ranking:

            1. get list of urls which the keyword points to for every keyword in the search string
            2. put url with its respective rank (in a dictionary)
                - create structure of url object:
                    {'url': '', 'title': '', 'description': ''}
                - multiply occurrence of that url with its precomputed rank
                - BONUS: if url was matched with its title to a keyword, + 1 for its computed rank
            3. create dictionary with rank as key, and url object as its value
            4. compare the ranks to sort and put in new dictionary to return (sorted_urls)
            
            Data sets: 
            --------------------------------------------------------
            sorted_urls: final sorted urls for passing to frontend
            urls_rank: number of times search keyword matched with the url
            urls_title: list of urls that had 1 or more matching strings in their title to a search keyword
            urls: list of urls from all keywords
        """
        sorted_urls = {};
        urls_rank = {};
        urls_title = [];
        urls = [];
        
        # Time start:
        start = clock();
        
        # Step 1
        self.__create_urls_obj(keyword, urls, urls_rank, urls_title);
        
        print "keywords: "
        pprint.pprint(keyword);
        print "urls_rank: "
        pprint.pprint(urls_rank);
        print "urls: "
        pprint.pprint(urls);
        print "url titles: "
        pprint.pprint(urls_title);
        
        if urls != None:
            # Step 2
            url_rank = self.__create_url_rank({}, urls, urls_rank, urls_title);
            
            print "url_ranks:"
            pprint.pprint(url_rank);
            
            # Step 3
            rank_url_obj = self.__create_rank_url_obj({}, url_rank);

            # Step 4
            sorted_urls = self.__create_sorted_urls({}, rank_url_obj, urls)

        # Time end:
        end = clock();
        
        return (sorted_urls, (end - start) * 1000);
    
    def __create_urls_obj(self, keywords, urls, urls_rank, urls_title):
        """
        urls_rank: number of times this url has matched with the different keywords
        e.g. the hamster lived
        if wikipedia.com has words for 'the' 'hamster' 'lived', then the value for urls_rank on wikipedia.com would be 3
        urls: array all urls which matched with the word
        Ranking by title: if the keyword appears in the title of that url, BONUS POINTS!! + 1
        """
        for keyword in keywords:
            keyword_urls = self.__textData.get_urls_from_word(keyword);
            
            if keyword_urls != None:
                for url in keyword_urls:
                    
                    # Get title, if keyword is in title, add url to the urls_title to grant BONUS
                    title = self.__textData.get_title_from_url(url);
                    title = [self.__searchResultsHelper.replace(x.lower()) for x in title.split(' ')];
                    if keyword in title:
                        if url not in urls_title:
                            urls_title.append(url);
                            
                    # Check and update occurrence of url in urls_rank
                    if url not in urls:
                        urls.append(url);
                        urls_rank[url] = 1;
                    else:
                        urls_rank[url] = urls_rank[url] + 1;
        
    def __create_url_rank(self, url_rank, urls, urls_rank, urls_title):
        for url in urls:
            rank = self.__pageRankData.get_page_rank(url);
            occurrences = urls_rank[url];
            bonus_points = 1.0 if url in urls_title else 0;
            url_rank[url] = rank * occurrences + bonus_points;
            
        return url_rank;
    
    def __create_rank_url_obj(self, rank_url_obj, url_rank):
        count = 0;
        for url, rank in url_rank.iteritems():
            url_obj = self.__get_url_obj(url);
            rank_url_obj[count] = dict({'rank': rank, 'url_obj': url_obj});
            count = count + 1;
             
        return rank_url_obj;
    
    def __create_sorted_urls(self, sorted_urls, rank_url_obj, urls):
        for n in range(0, len(urls)):
            highest_url_obj = {};
            highest_rank = float(0);
            highest_num = 0;
            counter = 0;

            for num, obj in rank_url_obj.iteritems():
                rank = obj['rank'];
                url_obj = obj['url_obj'];

                if counter == 0:
                    self.__deep_copy_dictionary(highest_url_obj, url_obj);
                    highest_rank = rank;
                    highest_num = num;
                else:
                    if rank > highest_rank:
                        self.__deep_copy_dictionary(highest_url_obj, url_obj);
                        highest_rank = rank;
                        highest_num = num;

                counter = counter + 1;

            if highest_rank != 0:
                sorted_urls[n] = highest_url_obj;
                del rank_url_obj[highest_num];  
        
        return sorted_urls;
                        
    # Splits the sorted urls into arrays of 5 to be passed back into the frontend
    def get_return_results(self, sorted_urls):
        # Array containing data for each search result page (ie arrays of 5)
        search_results = []

        num_results = len(sorted_urls)
        num_pages = math.ceil(num_results/5.0)

        # Keep track of how many results in a page
        result_count = 0
        # Array to go into search results (holds max of 5 url objects)
        results_per_page = []

        # Iterate through sorted urls and adds to each page array 
        for key, value in sorted_urls.iteritems():
            if result_count < 5:
                results_per_page.append(value)
                result_count += 1
            else:
                search_results.append(results_per_page)
                results_per_page = [value]
                result_count = 1

        if len(search_results) < num_pages:
            search_results.append(results_per_page)

        return search_results


    def __get_url_obj(self, url):
        title = self.__textData.get_title_from_url(url);
        desc = self.__textData.get_description_from_url(url);

        url_obj = dict(
                        {'url': url,
                         'title': title,
                         'desc': desc
                        });
        return url_obj

    def __deep_copy_dictionary(self, copy, src):
        copy['url'] = src['url'];
        copy['title'] = src['title'];
        copy['description'] = src['desc'];
