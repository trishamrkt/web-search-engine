# csc326-project

-------------------------------------------------
AMAZON WEB SERVICES INFORMATION:
-------------------------------------------------
Public IP Address: 54.174.107.175

To Access:
- Go to http://ec2-54-174-107-175.compute-1.amazonaws.com/

Instance setup script:
- Found in /AWSInstances/InitializeInstances.py

-------------------------------------------------
BENCHMARK SETUP:
-------------------------------------------------
The following commands were used to perform preliminary
benchmarking of our application:

RESULTS AVAILABLE AT:
- Lab2: RESULTS.pdf
- Lab3: RESULTS-LAB3.pdf

1. Analyzing Application Performance: <br>
  $ ab -n 318 -c 318 http://54.174.107.175/?keywords=helloworld+foo+bar

2. Anyalyzing CPU performance: <br>
  $ dstat --cpu -d --mem --net -io <br>
  $ ab -n 1000 -c318 http://54.174.107.175/?keywords=helloworld+foo+bar

NOTE: The results of our performance analysis can be found in RESULTS.docx

-------------------------------------------------
HOW TO USE:
-------------------------------------------------
DOWNLOADING EXTERNAL PACKAGES:
-------------------------------------------------
Enter the following commands in:<br>
  Terminal (Mac)
  Command Prompt (Windows)

1. Installing Bottle Framework:<br>
   $ pip install bottle

2. Installing BeautifulSoup Library (V 4.6.0)<br>
   $ pip install beautifulsoup4

3. Installing NumPy (V 1.13.3)<br>
   $ pip install numpy

4. Installing Beaker<br>
   $ pip install Beaker

5. Installing OAuth2 Library <br>
   $ pip install oauth2client

6. Instaling Google API Client for Python<br>
   $ pip install --upgrade google-api-python-client

5. Install http2 (AMI Linux dependency)<br>
   $ pip install httplib2

6. Install PyMongo <br>
    $ pip install pymongo
   
7. Install NYT Articles API
    $ pip install nytiesarticle

8. Install Weather API
    $ pip install weather-api
    
NOTE: For MAC users installing OAuth2 Library
- It is recommended to use a virtual environment for the command line
so as not to conflict with existing files during the oauth2client installation
process
- Can install virtual environment with the following command:
   $ pip install virtualenv

-------------------------------------------------
RUNNING WEB APPLICATION ON LOCAL MACHINE:
-------------------------------------------------
Code Alterations:
1. In /MainApp.py:
  - Change Bottle Script to run with host='localhost' and port='8000'
  - Change Google Redirect URL in Flow class initialization to redirect_uri='http://localhost:8000/redirect'
  - Change Google CLIENT_ID and CLIENT_SECRET to correct values

Running Application:
2. Enter ' $ python MainApp.py ' in:
  Terminal (Mac)
  Command Prompt (Windows)
2. Open up web browser. Navigate to 'localhost:8000'
3. Enter search string in input box.

Anonymous Mode:
  - The results table with words and their word counts will be displayed

Signed_in Mode:
  - Results table, 20 most popular keyword searches, and 10 most recent words will be displayed
  - Your search history will be saved for every subsequent login

-------------------------------------------------
TESTING:
-------------------------------------------------
- There are three files used for testing the application, one for front-end and
two for back-end.

Front-end:
- Lab 1: Tests the results obtained from the user's input query
    (ie words and their word counts)
- Lab 1: Tests the history of user inputs
    (ie correctness of the top twenty searched keywords)

Back-end:
- Lab 1: Tests get_inverted_index() and get_resolved_inverted_index() functions.
- Lab 2: Tests functionality of session management class
------------------------------------------------
How to Test:
------------------------------------------------
1. On the command line, navigate to the project directory.<br>
    $ cd /path/to/project/directory
2. Testing Front-end and Back-end functionalities<br>
   Run the following commands:
   
   LAB 3: PAGERANK TESTS: <br>
   $ python -m UnitTests.PageRankCrawlerTests
   
   LAB 1 & 2: CRAWLER & RESULTSPAGE TESTS: <br>
-  Front-end:<br>
    $ python -m UnitTests.ResultsPageServicesTest
-  Back-end:<br>
    $ python -m UnitTests.WebScrapingServicesTest
-  Session Management:<br>
    $ python -m UnitTests.UserSessionManagerTests
-----------------------------------------
IMPORTANT: before run Back-end unit test, start application by running (from project root):
- $ python MainApp.py & (only necessary for lab 1 & 2 unittests)
