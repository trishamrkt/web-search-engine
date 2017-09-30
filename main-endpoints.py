from bottle import *

@route('/')
def root_path():
    return template('index')

@route('/query')
def word_count():
    word_data = {};
    search_string = request.query['keywords'];
    html = '<link type="text/css" rel="stylesheet" href="/static/css/style.css"\>'

    html = html + '<h1>Search for ' + search_string + '</h1>';
    html = html + '<table>'
    html = html + '<tr><td>Word</td><td>Count</td></tr>'

    keywords = search_string.split(' ');

    # Put words and word count into dictionary
    for word in keywords:
        if word in word_data.keys():
            word_data[word] += 1;
        else:
            word_data[word] = 1;

    # Create HTML table with words and their word counts
    for key in word_data.keys():
        html = html + '<tr><td>' + key + '</td>' + '<td>' + str(word_data[key]) + '</td></tr>'

    html = html + '</table>'
    return html;

@get('/static/css/<filepath:re:.*\.css>')
def static(filepath):
    return static_file(filepath, root='static/css')

run(host='localhost', port=8000, debug=True);
