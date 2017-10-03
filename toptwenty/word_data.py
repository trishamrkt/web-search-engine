from toptwenty import TopTwenty

# This class does parses the keywords when the user inputs a search string
class WordData():
    def __init__(self):
        self.wordData = {};
        self.html = '';

    # inserts words into a table in html format
    def get_table_html(self, searchString, allWords):
        self.html = self.html + '<h1 class="table-header">search for ' + searchString + '</h1>';
        self.html = self.html + '<table class="word-table" id="results">'
        self.html = self.html + '<tr class="col-title"><th>word</th><th>count</th></tr>'

        keywords = searchString.split(' ');
        uniqueWords = [];

        # Put words and word count into dictionary
        for word in keywords:
            if word in self.wordData.keys():
                self.wordData[word] += 1;
            else:
                uniqueWords.append(word)
                self.wordData[word] = 1;

        # Create HTML table with words and their word counts
        for word in uniqueWords:
            allWords.add_word(word, self.wordData[word]);
            self.html = self.html + '<tr class="word-data"><td class="word">' + word + '</td>' + '<td class="count">' + str(self.wordData[word]) + '</td></tr>'

        self.html = self.html + '</table>'
        return self.html;
