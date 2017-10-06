from ResultsPageServices.WordData import WordData
from ResultsPageServices.TopTwenty import TopTwenty
import unittest

class ResultsPageServicesTest(unittest.TestCase):

    def setUp(self):
        self.word_data = WordData()
        self.history = TopTwenty()
        return

    def tearDown(self):
        return

    # Test template for testing results table
    # Params - test_string - represent search query
    #        - expected values in results table returned as a dict
    def results_test_template(self, test_string, expected):
        # Get result from functions we wrote
        self.word_data.add_words(test_string);
        actual = self.word_data.get_word_data();

        # Compare to expected result
        self.assertEqual(expected, actual)

        # Reset word_data
        self.word_data.clear_word_data();
        return

    # Simple test - no duplicates, no extra whitespace
    def test_results_one(self):
        test_string = "Hello World!"
        expected_result = {'hello' : 1, 'world!' : 1};
        self.results_test_template(test_string, expected_result)
        return

    # Test for strings with only spaces
    def test_results_two(self):
        test_string = "        "
        expected_result = {};
        self.results_test_template(test_string, expected_result)
        return

    # Test for empty string
    def test_results_three(self):
        test_string = ""
        expected_result = {}
        self.results_test_template(test_string, expected_result)
        return

    # Test for strings with duplicates
    def test_results_three(self):
        test_string = "csc326 csc326 326 courses course course csc326"
        expected_result = {'csc326' : 3, 'courses' : 1, 'course' : 2, '326' : 1}
        self.results_test_template(test_string, expected_result);
        return

    # Test with extra white space at beginning, middle, and end of string
    def test_results_four(self):
        test_string = "     hello    world      !  "
        expected_result = {'hello' : 1, 'world' : 1, '!' : 1}
        self.results_test_template(test_string, expected_result)
        return

    # Test with upper and lowercase chars in string
    def test_results_five(self):
        test_string = "HeLlO hEllo heLLo HELLO";
        expected_result = {'hello' : 4}
        self.results_test_template(test_string, expected_result)
        return

    # ------- TESTS FOR SEARCH HISTORY DATA ------- #
    # Test template for testing history
    # Params - list of strings - represent separate search queries
    #        - expected return value of dict
    def history_test_template(self, strings, expected):
        for string in strings:
            temp_data = WordData();
            temp_data.add_words(string);
            temp_data.get_table_html(string, self.history);

        actual = self.history.get_top();

        self.assertEqual(expected, actual)
        return

    # Simple test - multiple string inputs with duplicate words
    def test_history_one(self):
        test_strings = ['Hello world', 'hello hello hello', 'world', 'thank you']
        expected_result = {'hello' : 4, 'world' : 2, 'thank' : 1, 'you' : 1}
        self.history_test_template(test_strings, expected_result);
        return

    # > 20 unique word inputs - only the top 20 most frequent are in expected dict
    # '1' only displayed once, 2-21 displayed > 1 times so they should be in the dict
    def test_history_two(self):
        test_strings = ['1', '2 2', '3 3', '4 4', '5 5', '6 6', '7 7', '8 8', '9 9', '10 10', '11 11',
                        '12 12', '13 13', '14 14', '15 15', '16 16', '17 17', '18 18', '19 19', '20', '20', '20 20 20 20 20 20', '21 21']

        expected_result = {'2' : 2, '3' : 2, '4' : 2, '5' : 2, '6' : 2, '7' : 2, '8' : 2, '9' : 2, '10' : 2, '11' : 2,
                        '12' : 2, '13' : 2, '14' : 2, '15' : 2, '16' : 2, '17' : 2, '18' : 2, '19' : 2, '20': 8, '21' : 2}
        self.history_test_template(test_strings, expected_result);
        return

    # No inputs strings
    def test_history_three(self):
        test_strings = []
        expected_result = {}
        self.history_test_template(test_strings, expected_result);
        return

    # All empty strings/all whitespace
    def test_history_four(self):
        test_strings = ['', '', '    ', ''];
        expected_result = {};
        self.history_test_template(test_strings, expected_result);
        return

if __name__ == "__main__":
    unittest.main()
