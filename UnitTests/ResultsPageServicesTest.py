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
        test_string = "     hello world      !  "
        expected_result = {'hello' : 1, 'world' : 1, '!' : 1}
        self.results_test_template(test_string, expected_result)
        return

    # Test with upper and lowercase chars in string
    def test_results_five(self):
        test_string = "HeLlO hEllo heLLo HELLO";
        expected_result = {'hello' : 4}
        self.results_test_template(test_string, expected_result)
        return

    # Test template for testing history
    def history_test_template(self, strings, expected):
        for string in strings:
            temp_data = WordData();
            temp_data.add_words(string);
            temp_data.get_table_html(string, self.history);

        actual = self.history.get_top();

        self.assertEqual(expected, actual)
        return

    def test_history_data(self):
        test_strings = ['Hello world', 'hello hello hello', 'world', 'thank you']
        expected_result = {'hello' : 4, 'world' : 2, 'thank' : 1, 'you' : 1}
        self.history_test_template(test_strings, expected_result);
        return

if __name__ == "__main__":
    unittest.main()
