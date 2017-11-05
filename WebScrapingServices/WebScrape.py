from bs4 import BeautifulSoup
import requests as requests
import re
import pprint 
from WebScrapePersistHelper import WebScrapePersistHelper

# Beautiful Soup API calls
class WebScrape():

    def __init__(self, textData, pageRankData):
        self.__persistHelper = WebScrapePersistHelper(textData, pageRankData);
        
        self.__docId_to_url = [];
        self.__words_per_document = [];
        self.__wordId_to_word = [];
        self.__wordId_to_docIds = {};
        self.__word_to_url = {};
        self.__url_to_title = {};
        self.__url_to_description = {};
        
        self.__inbound = {};
        # We must get the original outbound to compute the new inbound
        self.__outbound = self.__persistHelper.getOutbound();
        self.__num_links = {};
    
    
    def scrape_the_web(self, url_list):
        # Modify url_list to include only urls which are not present in database
        new_list = self.__persistHelper.parse_url(url_list);
        
        if len(new_list) != 0:
            self.__beautiful_soup_controller(new_list, url_list);
            self.__print_in_memory_datastructures();
    
            # Persist to database
            self.__persist_to_db();
            self.__clear_in_memory_datastructures();
            
            print "DONE PERSISTENCE AND MEMORY CLEAR!"
        else:
            print "No new urls - skipping web scraping and persistence"
            
        return
    
    def __beautiful_soup_controller(self, new_list, old_list):
        """
        Scrapes web using beautifulsoup API
        Constructs in-memory data structures from the given url_list
        new_list: list of urls not in database
        old_list: all urls (not in db + already in db)
        """
        # load all words of one url into an array (separation by spaces), and is contained in a bigger array indexed by document ids
        self.__docId_to_url = new_list;
        
        # Scrape all urls for their href links (inbound, outbound datastructures)
        for url in old_list:
            soup = self.__call_beautiful_soup(url);
            self.__parse_href_text(soup, url, old_list);
        
        # Scrape new urls to add them to other datastructures
        for url in new_list:
            array = [];
            soup = self.__call_beautiful_soup(url);
            array = self.__parse_soup_text(soup, url);
            self.__words_per_document.append(array);
        
        self.__construct_inbound(old_list);
        
        # 1. separate words into individual indices, keeping uniqueness
        # 2. putting common words between documents in single pair of a dictionary
        for document in self.__words_per_document:
            doc_id = self.__words_per_document.index(document);
            
            for word in document:
                
                # 1
                if word not in self.__wordId_to_word:
                    self.__wordId_to_word.append(word);
                    index = self.__wordId_to_word.index(word);

                    # 2
                    self.__wordId_to_docIds[index] = set();
                    self.__wordId_to_docIds[index].add(doc_id);

                else:
                    # 2
                    index = self.__wordId_to_word.index(word);
                    if self.__words_per_document.index(document) not in self.__wordId_to_docIds[index]:
                        self.__wordId_to_docIds[index].add(doc_id);

        self.__get_resolved_inverted_index();
        
    def __persist_to_db(self):
        self.__persistHelper.persist_docId_to_url(self.__docId_to_url);
        self.__persistHelper.persist_wordId_to_word(self.__wordId_to_word);
        self.__persistHelper.persist_wordId_to_docIds(self.__wordId_to_docIds, self.__wordId_to_word);
        self.__persistHelper.persist_word_to_url(self.__word_to_url);
        
        self.__persistHelper.persist_inbound(self.__inbound);
        self.__persistHelper.persist_outbound(self.__outbound);
        self.__persistHelper.persist_num_links(self.__num_links);
        
        self.__persistHelper.persist_url_to_title(self.__url_to_title);
        self.__persistHelper.persist_url_to_description(self.__url_to_description);
        
        return
    
    def __get_resolved_inverted_index(self):        
        # mapping real words and doc urls with their id's and putting them in a dictionary (as specified for Lab1)
        for word_id, doc_ids in self.__wordId_to_docIds.iteritems():
            word = self.__wordId_to_word[word_id];
            docs = set();
            
            for doc_id in doc_ids:
                docs.add(self.__docId_to_url[doc_id]);
            
            self.__word_to_url[word] = docs;
            
    def __call_beautiful_soup(self, url):
        r = requests.get(url);
        data = r.content.decode('utf-8', 'ignore');
        soup = BeautifulSoup(data, 'html.parser');
        
        return soup

    def __parse_soup_text(self, soup, url):
        [s.extract() for s in soup(['iframe', 'meta', 'script', 'style'])]

        title = str(soup.findAll('title')[0]);
        body = soup.find('body');
        
        # Generate title for website
        print "Title: " + title;
        if url not in self.__url_to_title and title != None:
            title = title.replace('<title>', '').replace('</title>', '');
            self.__url_to_title[url] = title;
        
        description = '';
        word_count = 25;
        start_counting = False;
        list = [];
        for tag in body.findAll():
            inner_list = tag.text.split();
            for word in inner_list:
                
                # Getting description: (take 25 words, starts after a period has been encountered)
                # If there was a nonascii character in the text, restart
                if word_count > 0:
                    if self.__is_ascii_encoded(word) and self.__is_valid_word(word) and start_counting:
                        description = description + ' ' + word;
                        word_count = word_count - 1;
                    else:
                        word_count = 25;
                        description = '';
                        start_counting = False;
                if '.' in word:
                    start_counting = True;
                
                if word:
                    parsed = word.replace('\n','').replace('\t', '').replace('\r', '').replace(',', '').replace('.', '').strip();
                    list.append(parsed);
        
        description = description + '...';
        print description;
        if url not in self.__url_to_description:
            self.__url_to_description[url] = description;
        
        return list;
    
    def __is_ascii_encoded(self, word):
        try:
            word.decode('ascii');
        except (UnicodeEncodeError, UnicodeDecodeError) as e:
            return False;
        else:
            return True;
        
        
    def __parse_href_text(self, soup, url, old_list):
        [s.extract() for s in soup(['iframe', 'script', 'meta', 'style'])]
        
        a_tags = soup.findAll('a', href=True);
        
        # Construct out bound links to current link from Beautiful Soup
        self.__construct_outbound(a_tags, url, old_list);
        self.__num_links[url] = len(a_tags);
                
    def __construct_inbound(self, url_list):
        """
        Let current url be 'x':
        if 'x' exists in the set of outbound urls to a url 'y' (within the list of available urls)
        then 'y' is an inbound url to 'x'
        """
        for x in url_list:
            if x not in self.__inbound:
                self.__inbound[x] = [];

            for y in url_list:

                # If y is not the same as x, and y is in part of the outbound structure
                if y != x and y in self.__outbound:

                    # If x is in the outbound of y, and y has not been inserted as an inbound url of x already
                    if x in self.__outbound[y] and y not in self.__inbound[x]:
                        self.__inbound[x].append(y);

        return

    def __construct_outbound(self, a_tags, url, url_list):
        """
        Traverses each 'a' tag in url document and find the url which matches the
        url_list given, and puts that in the outbound datastructure
        Criteria:
            - Exclude links to itself
            - All outbound urls are unique (exclude ones which appear more than once in document)
        """
        for link in a_tags:
            # Transform links to proper format

            new_link = link['href'];
            if new_link.find('wikipedia.org') == -1:
                new_link = 'https://en.wikipedia.org' + new_link;

            # Check if link is in URL_list, if yes, put it into outbound list

            if new_link in url_list:
                if url not in self.__outbound:
                    self.__outbound[url] = [];

                if new_link != url and new_link not in self.__outbound[url]:
                    self.__outbound[url].append(new_link);

    # further polish words, excluding certain characters within words (such as commas, etc.)
    def __cleanup_word(self, old_word):
        new_word = old_word.replace(',', '').replace('.', '').replace('<', '').replace('>', '').replace('?', '');
        return new_word

    def __is_valid_word(self, word):
         if (';' not in word) and ('&' not in word) and ('<' not in word) and ('>' not in word) \
            and ('-' not in word) and ('(' not in word) and (')' not in word) and ('_' not in word) \
            and ('\\' not in word) and ('/' not in word) and ('}' not in word) and ('{' not in word) \
            and ('=' not in word) and ('$' not in word) and ('meta' not in word) \
            and ('charset' not in word) and ('script' not in word) and ('#' not in word) and ('=' not in word) \
            and ('|' not in word) and not self.__numbers_in_word(word):
             return True;
         else:
             return False;
    
    def __numbers_in_word(self, word):
        if ('0' in word or '1' in word or '2' in word or '3' in word or '4' in word or '5' in word \
            or '6' in word or '7' in word or '8' in word or '9' in word) and ('f' in word or 'e' in word \
            or 'u' in word):
            return True;
        else:
            return False;
        
    def __parse_document(self, document):
        document = re.sub('<([^>]*)>', '', document.prettify());
        return document;
    
    def __print_in_memory_datastructures(self):
        pprint.pprint(self.__docId_to_url);
          
        pprint.pprint(self.__inbound);
        pprint.pprint(self.__outbound);
        pprint.pprint(self.__num_links);
        pprint.pprint(self.__url_to_title);
        pprint.pprint(self.__url_to_description);
            
    def __clear_in_memory_datastructures(self):
        del self.__docId_to_url[:];
        del self.__words_per_document[:];
        del self.__wordId_to_word[:];
        self.__wordId_to_docIds.clear();
        self.__word_to_url.clear();
        self.__inbound.clear();
        self.__outbound.clear();
        self.__num_links.clear();
        self.__url_to_description.clear();
        self.__url_to_title.clear();
        
    