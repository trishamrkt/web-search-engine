# This class contains info about the top twenty most popular keywords
class TopTwenty():
    def __init__(self):
        # Contains all the words that have been searched
        self.searched = {};

        # Contains the top twenty words that have been searched
        self.top = {};

    # add word to dictionaries
    def add_word(self, word, count):
        # increase count of words in the searched dict
        if word in self.searched.keys():
            self.searched[word] += count;
        else:
            self.searched[word] = count;

        # Gets the new word count of the current word
        newWordCount = self.searched[word];

        # Length of top twenty dictionary
        topLength = len(self.top)

        # Checks if the top twenty dictionary is empty
        # If not stores the keys with the max and min values
        if not topLength == 0:
            maxKey = max(self.top);
            minKey = min(self.top);

        # Check if word is one of the 20 most popular
        if topLength < 20:
            if word not in self.top.keys():
                self.top[word] = count;
            elif word in self.top.keys():
                self.top[word] += count;

        # Check if the current word has higher count than
        # largest and smallest counts in top twenty
        elif newWordCount >= self.top[maxKey] or newWordCount > self.top[minKey]:
            if word in self.top.keys():
                self.top[word] += count;
            else:
                self.top[word] = newWordCount;
                del self.top[minKey]

    def get_searched(self):
        return self.searched;

    def get_top(self):
        return self.top;

    # Puts top twenty dictionary data into an HTML table
    def get_popular_table_html(self):
        html = '<h1 class="table-header">top 20 searched words:</h1><table class="word-table" id="history"><tr class="col-title"><th>word</th><th>count</th></tr>'
        for key, value in sorted(self.top.items(), key=lambda (k,v): (v,k), reverse=True):
            html = html + '<tr class="word-data"><td class="word">' + key + '</td><td class="count">' + str(value) + '</td></tr>'

        html = html + "</table>"
        return html

    def get_searched_table_html(self):
        html = '<h1 class="table-header">10 most recent searches:</h1> \
                <table class="word-table" id="searched">\
                    <tr class="col-title"><th>word</th></tr>';
        for key in self.searched.keys()[:10]:
            html += '<tr class="word-data"><td class="word">' + key + '</td></tr>';

        html = html + "</table>";
        return html

    def set_searched(self, __searched):
        self.searched = __searched;

    def set_top(self, __top):
        self.top = __top;

    def clear_history(self):
        self.searched = {};
        self.top = {};
        return
