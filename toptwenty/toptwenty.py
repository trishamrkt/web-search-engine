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
        new_word_count = self.searched[word];

        # Length of top twenty dictionary
        top_length = len(self.top)

        # Checks if the top twenty dictionary is empty
        # If not stores the keys with the max and min values
        if not top_length == 0:
            max_key = max(self.top);
            min_key = min(self.top);

        # Check if word is one of the 20 most popular
        # If there are less than 20 words that have been word - go in most popular
        # by default
        if top_length < 20:
            if word not in self.top.keys():
                self.top[word] = count;
            elif word in self.top.keys():
                self.top[word] += count;

        # Else check if the current word has higher count than
        # largest and smallest counts in top twenty
        elif new_word_count >= self.top[max_key] or new_word_count > self.top[min_key]:
            if word in self.top.keys():
                self.top[word] += count;
            else:
                self.top[word] = new_word_count;
                del self.top[min_key]

    # Puts top twenty dictionary data into an HTML table
    def get_table_html(self):
        html = '<h1 class="table-header">top 20 searched words:</h1><table class="word-table" id="history"><tr class="col-title"><th>word</th><th>count</th></tr>'
        for key, value in sorted(self.top.items(), key=lambda (k,v): (v,k), reverse=True):
            html = html + '<tr class="word-data"><td class="word">' + key + '</td><td class="count">' + str(value) + '</td></tr>'

        html = html + "</table>"
        return html
