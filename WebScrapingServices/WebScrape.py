from bs4 import BeautifulSoup
import requests as requests
import re

# Beautiful Soup API calls
class WebScrape():

    def __init__(self, textData, pageRankData):
        self.__textData = textData;
        self.__pageRankData = pageRankData;
        self.__docId_to_url = self.__textData.getDocId_to_url();
        self.__words_per_document = self.__textData.getWords_per_document();
        self.__wordId_to_word = self.__textData.getWordId_to_word();
        self.__wordId_to_docIds = self.__textData.getWordId_to_DocIds();
        self.__inbound = self.__pageRankData.getInbound();
        self.__outbound = self.__pageRankData.getOutbound();
        self.__num_links = self.__pageRankData.getNumLinks();

    def scrape_the_web(self, url_list):
        # load all words of one url into an array (separation by spaces), and is contained in a bigger array indexed by document ids
        for url in url_list:
            array = [];
            array = self.__call_beautiful_soup(url, url_list, array);
            self.__words_per_document.append(array);

        self.__construct_inbound(url_list);


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

        return

    def __call_beautiful_soup(self, url, url_list, array):
        r = requests.get(url);
        data = r.content;
        soup = BeautifulSoup(data, 'html.parser');

        array = self.__parse_soup_text(soup, url, url_list);
        return array;

    def __parse_soup_text(self, soup, url, url_list):
        [s.extract() for s in soup(['iframe', 'script', 'meta', 'style'])]

        body = soup.find('body');
        a_tags = soup.findAll('a', href=True);

        # Construct out bound links to current link from Beautiful Soup
        self.__construct_outbound(a_tags, url, url_list);
        self.__num_links[url] = len(a_tags);

        list = [];
        for tag in body.findAll():

            inner_list = tag.text.split();
            for word in inner_list:
                if word:
                    parsed = word.replace('\n','').replace('\t', '').replace('\r', '').replace(',', '').replace('.', '').strip();
                    list.append(parsed);

        return list;

    
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
            and ('|' not in word):
             return True;
         else:
             return False;

    def __parse_document(self, document):
        document = re.sub('<([^>]*)>', '', document.prettify());
        return document;
