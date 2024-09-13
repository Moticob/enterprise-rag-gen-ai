from langchain.chains import RetrievalQA
from openai_client import OpenAIClient
from pinecone_client import PineconeClient

class RAGEngine:
    def __init__(self):
        # Initialize OpenAI and Pinecone clients
        self.openai_client = OpenAIClient()
        self.pinecone_client = PineconeClient()

        # Initialize the LangChain retrieval-based Q&A system
        self.qa_chain = RetrievalQA(llm=self.openai_client.get_llm(), retriever=self.pinecone_client.get_retriever())

    def get_response(self, query):
        # Retrieve context from Pinecone and generate response from GPT-4
        response = self.qa_chain.run(query)
        return response

