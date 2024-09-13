import unittest
from backend.rag_engine import RAGEngine

class TestRAGEngine(unittest.TestCase):
    def setUp(self):
        self.engine = RAGEngine()

    def test_get_response(self):
        user_query = "How can we optimize our supply chain?"
        response = self.engine.get_response(user_query)
        self.assertIsNotNone(response)
        self.assertIsInstance(response, str)

if __name__ == "__main__":
    unittest.main()

