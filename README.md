# csc326-project
-------------------------------------------------
HOW TO USE:
-------------------------------------------------
DOWNLOADING EXTERNAL PACKAGES:
-------------------------------------------------
Enter the following commands in:
  Terminal (Mac)
  Command Prompt (Windows)

1. Installing Bottle Framework:
  $ pip install bottle

2. Installing BeautifulSoup Library (V 4.6.0)
  $ pip install beautifulsoup4
  
3. Installing PyNum (V 1.13.3)
  $ pip install numpy

-------------------------------------------------
RUNNING WEB APPLICATION:
-------------------------------------------------
1. Enter ' $ python MainApp.py ' in:
  Terminal (Mac)
  Command Prompt (Windows)
2. Open up web browser. Navigate to 'localhost:8000'
3. Enter search string in input box.
  - The results and history data tables will then be displayed to you.
  - To return to the search page, click on the logo in the top left hand corner of the web page.

-------------------------------------------------
TESTING:
-------------------------------------------------
- There are two files used for testing the application, one for front-end and
one for back-end.

Front-end:
- Tests the results obtained from the user's input query
    (ie words and their word counts)
- Tests the history of user inputs
    (ie correctness of the top twenty searched keywords)

Back-end:
- Tests get_inverted_index() and get_resolved_inverted_index() functions.

------------------------------------------------
How to Test:
------------------------------------------------
1. On the command line, navigate to the project directory.
    $ cd /path/to/project/directory
2. Testing Front-end and Back-end functionalities
   Run the following commands:
a) Front-end:
    $ python -m UnitTests.ResultsPageServicesTest
b) Back-end:
    $ python -m UnitTests.WebScrapingServicesTest
    
    IMPORTANT: before run Back-end unit test, start application by running (from project root): 
    $ python MainApp.py &
