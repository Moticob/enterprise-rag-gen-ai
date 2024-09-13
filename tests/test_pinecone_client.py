import unittest
from backend.pinecone_client import PineconeClient

class TestPineconeClient(unittest.TestCase):
    def setUp(self):
        self.client = PineconeClient()

    def test_get_retriever(self):
        retriever = self.client.get_retriever()
        self.assertIsNotNone(retriever)

    def test_add_document(self):
        document = {
            "id": "test_doc",
            "text": "This is a test document about business strategies."
        }
        self.client.add_document(document)
        # Check if the document is correctly added (add more tests based on the actual use case)

if __name__ == "__main__":
    unittest.main()

