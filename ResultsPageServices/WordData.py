from ResultsPageServices.TopTwenty import TopTwenty

# This class does parses the keywords when the user inputs a search string
class WordData():
    def __init__(self):
        self.wordData = {};
        self.html = '';
        self.uniqueWords = [];


    def add_words(self, searchString):
        stripped = searchString.strip().lower();

        if stripped == '':
            return

        keywords = stripped.split(' ');

        # Put words and word count into dictionary
        for word in keywords:
            if word != '':
                if word in self.wordData.keys():
                    self.wordData[word] += 1;
                else:
                    self.uniqueWords.append(word)
                    self.wordData[word] = 1;

    # inserts words into a table in html format
    def get_table_html(self, searchString, allWords=TopTwenty()):
        self.html = self.html + '<h1 class="table-header">search for ' + searchString + '</h1>';
        self.html = self.html + '<table class="word-table" id="results">'
        self.html = self.html + '<tr class="col-title"><th>word</th><th>count</th></tr>'

        # Create HTML table with words and their word counts
        for word in self.uniqueWords:
            allWords.add_word(word, self.wordData[word]);
            self.html = self.html + '<tr class="word-data"><td class="word">' + word + '</td>' + '<td class="count">' + str(self.wordData[word]) + '</td></tr>'

        self.html = self.html + '</table>'
        return self.html;

    # Accessors
    def get_word_data(self):
        return self.wordData

    def clear_word_data(self):
        self.wordData = {};
