import streamlit as st
from backend.rag_engine import RAGEngine
import plotly.express as px
import pandas as pd

# Initialize RAG Engine
engine = RAGEngine()

# Set up the Streamlit interface
st.set_page_config(page_title="Enterprise AI Decision-Maker", page_icon=":chart_with_upwards_trend:")

# Custom CSS for better styling
with open("frontend/assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Display title and description
st.title("Enterprise AI Decision-Maker")
st.write("Revolutionize your business decisions with Generative AI and Retrieval-Augmented Generation (RAG).")

# Image/logo placeholder (optional)
st.image("frontend/assets/logo.png", width=150)

# User query input
user_query = st.text_input("Ask a business-related question (e.g., 'How can we optimize our supply chain?'):")

# If user submits a query
if user_query:
    # Get AI-generated response using the RAG Engine
    with st.spinner("Generating strategy..."):
        response = engine.get_response(user_query)

    # Display the AI's recommendation
    st.subheader("AI's Recommendation:")
    st.write(response)

    # Mock data for visualization (to be replaced by actual business data)
    mock_data = {
        "Metric": ["Revenue", "Cost Reduction", "Customer Satisfaction", "Market Share"],
        "Before AI": [50, 30, 60, 25],
        "After AI": [70, 50, 85, 35],
    }
    df = pd.DataFrame(mock_data)

    # Plot the data
    fig = px.bar(df, x="Metric", y=["Before AI", "After AI"], barmode="group", title="Business Impact Metrics")
    st.plotly_chart(fig)

# Sidebar for additional information
st.sidebar.title("About the Project")
st.sidebar.write("""
This tool utilizes GPT-4 and Pinecone for context-aware business decision-making. It combines generative AI with retrieval-augmented generation (RAG) to deliver actionable insights based on real-time business data.
""")

st.sidebar.write("Made by: Your Team")

# Footer
st.markdown("""
<footer style="text-align:center; font-size:small;">
    &copy; 2024 Enterprise AI Decision-Maker | Powered by GPT-4 & Pinecone
</footer>
""", unsafe_allow_html=True)

