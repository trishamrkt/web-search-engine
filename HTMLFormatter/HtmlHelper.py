from ResultsPageServices.WordData import WordData
from ResultsPageServices.TopTwenty import TopTwenty

# Declare constants for HTML
TABLE_STYLE = '<link type="text/css" rel="stylesheet" href="/static/css/word_table_data.css"\>'
NAVI_STYLE = '<link type="text/css" rel="stylesheet" href="/static/css/sign_in_buttons.css"\>'
STYLE = TABLE_STYLE + NAVI_STYLE
FONTS = '<link href="https://fonts.googleapis.com/css?family=Assistant" rel="stylesheet" >\
        <link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet"\>'

# Return HTML for Anonymous mode
def anonymous_results(search_string):
    NAV = create_nav_bar('', False);

    word_data = WordData();
    word_data.add_words(search_string);
    table_html = word_data.get_table_html(search_string)
    html = STYLE + FONTS + NAV + table_html;
    return html;

# Return HTML for Signed In Mode
def signed_in_results(search_string, history, most_recent, email):
    NAV = create_nav_bar(email, True);

    word_data = WordData();
    top_twenty = TopTwenty()
    word_data.add_words(search_string);

    top_twenty.set_top(history);
    top_twenty.set_searched(most_recent)

    # Get HTML for the results page
    word_count_table_html = word_data.get_table_html(search_string.strip(), top_twenty);
    top_twenty_table_html = top_twenty.get_popular_table_html();
    most_recent_table_html = top_twenty.get_searched_table_html();
    html = STYLE + FONTS + NAV + word_count_table_html + top_twenty_table_html + most_recent_table_html;

    top_twenty_data = top_twenty.get_top();
    most_recent_data = top_twenty.get_searched();

    return [html, top_twenty_data, most_recent_data];

def create_nav_bar(email, signed_in):
    if signed_in:
        account = email;
    else:
        account = "Sign In";

    nav = '<nav class="navi">\
                <a href="/" id="googao-title">Googao</a>\
                <a href="/logout" class="account-buttons results-acc-buttons">Sign Out</a>\
                <a href="/login" class="account-buttons results-acc-buttons">' + account + '</a>\
           </nav>'

    return nav
