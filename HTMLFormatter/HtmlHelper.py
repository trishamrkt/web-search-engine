from ResultsPageServices.WordData import WordData

# Returns HTML for results page
def results_html(searchString, mostPopular):
    wordData = WordData();
    wordData.add_words(searchString)

    # Gets HTML for table with words and their word counts
    html = '<link type="text/css" rel="stylesheet" href="/static/css/word_table_data.css"\>'
    html += "<link href='https://fonts.googleapis.com/css?family=Assistant' rel='stylesheet'>"
    html += '<nav class="navi"><a href="/">Googao</a></nav>'
    html = html + wordData.get_table_html(searchString.strip(), mostPopular);
    html = html + mostPopular.get_table_html();
    return html;
