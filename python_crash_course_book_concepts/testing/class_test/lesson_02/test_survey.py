import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey
     the setup method will one time we can use many methods.
    """

    def setUp(self):
        """Creating the surveys and responses to use all test methods """
        question = "What language did you first learn to speak ?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['telugu', 'tamil', 'english']

    def test_store_single_response(self):
        """Test the single response and stored properly"""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test the three response and stored properly"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
