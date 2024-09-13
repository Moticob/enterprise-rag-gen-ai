import pinecone
import yaml

class PineconeClient:
    def __init__(self):
        # Load Pinecone API Key from secrets.yaml
        with open("config/secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)

        self.api_key = secrets['pinecone_api_key']
        self.index_name = secrets.get('pinecone_index', 'business-data-index')

        # Initialize Pinecone
        pinecone.init(api_key=self.api_key, environment='us-west1-gcp')
        self.index = pinecone.Index(self.index_name)

    def get_retriever(self):
        # Use LangChain Pinecone retriever integration
        from langchain.vectorstores import Pinecone
        return Pinecone(index=self.index)

    def add_document(self, document):
        # Add a new document to Pinecone
        vector = self._embed_document(document)
        self.index.upsert(vectors=[(document['id'], vector)])

    def _embed_document(self, document):
        # Convert the document into a vector using an embedding model
        from langchain.embeddings import OpenAIEmbeddings
        embeddings = OpenAIEmbeddings(openai_api_key=self.api_key)
        vector = embeddings.embed_text(document['text'])
        return vector

