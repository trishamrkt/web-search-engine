from toptwenty import TopTwenty

# This class does parses the keywords when the user inputs a search string 
class WordData():
    def __init__(self):
        self.word_data = {};
        self.html = '';

    # inserts words into a table in html format
    def get_table_html(self, search_string, all_words):
        self.html = '<link type="text/css" rel="stylesheet" href="/static/css/style.css"\>'

        self.html = self.html + '<h1>Search for ' + search_string + '</h1>';
        self.html = self.html + '<table>'
        self.html = self.html + '<tr><td>Word</td><td>Count</td></tr>'

        keywords = search_string.split(' ');

        # Put words and word count into dictionary
        for word in keywords:
            if word in self.word_data.keys():
                self.word_data[word] += 1;
            else:
                self.word_data[word] = 1;

        # Create HTML table with words and their word counts
        for key in self.word_data.keys():
            all_words.add_word(key, self.word_data[key]);
            self.html = self.html + '<tr><td>' + key + '</td>' + '<td>' + str(self.word_data[key]) + '</td></tr>'

        self.html = self.html + '</table>'
        return self.html;
