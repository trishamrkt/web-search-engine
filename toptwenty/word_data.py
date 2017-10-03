from toptwenty import TopTwenty

# This class does parses the keywords when the user inputs a search string
class WordData():
    def __init__(self):
        self.word_data = {};
        self.html = '';

    # inserts words into a table in html format
    def get_table_html(self, search_string, all_words):
        self.html = self.html + '<h1 class="table-header">search for ' + search_string + '</h1>';
        self.html = self.html + '<table class="word-table" id="results">'
        self.html = self.html + '<tr class="col-title"><th>word</th><th>count</th></tr>'

        keywords = search_string.split(' ');
        unique_words = [];

        # Put words and word count into dictionary
        for word in keywords:
            if word in self.word_data.keys():
                self.word_data[word] += 1;
            else:
                unique_words.append(word)
                self.word_data[word] = 1;

        # Create HTML table with words and their word counts
        for word in unique_words:
            all_words.add_word(word, self.word_data[word]);
            self.html = self.html + '<tr class="word-data"><td class="word">' + word + '</td>' + '<td class="count">' + str(self.word_data[word]) + '</td></tr>'

        self.html = self.html + '</table>'
        return self.html;
