from rag_engine import RAGEngine

def main():
    # Initialize the RAG Engine
    engine = RAGEngine()

    # Example query from a business user
    user_query = "What strategies should we use to optimize our supply chain?"

    # Get the answer from the engine
    response = engine.get_response(user_query)

    # Output the AI's response
    print("AI's Recommendation:")
    print(response)

if __name__ == "__main__":
    main()

