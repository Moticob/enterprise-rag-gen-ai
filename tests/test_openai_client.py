import unittest
from backend.openai_client import OpenAIClient

class TestOpenAIClient(unittest.TestCase):
    def setUp(self):
        self.client = OpenAIClient()

    def test_generate_response(self):
        prompt = "What is the best strategy to increase market share?"
        response = self.client.generate_response(prompt)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()

