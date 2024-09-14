
# Enterprise RAG - Transform Business Process & Decision-Making with Generative AI

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Pinecone](https://img.shields.io/badge/Pinecone-00BFFF?style=for-the-badge&logo=pinecone&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)

## Overview
This project leverages Generative AI, specifically GPT-4, and Retrieval-Augmented Generation (RAG) to provide business insights and strategies based on company-specific data. The system integrates **OpenAI's GPT-4** with **Pinecone** vector storage to deliver real-time, context-aware insights to enterprise users.

## Features
- **LLM-Powered Engine**: Uses GPT-4 to generate business strategies based on user queries.
- **RAG Integration**: Combines AI generation with real-time document retrieval from Pinecone.
- **Interactive UI**: Streamlit-powered web app that allows users to ask questions and visualize business impacts.
- **Data Privacy**: Secure handling of business-sensitive information.

## Tech Stack
- **Backend**: Python, OpenAI API, Pinecone, LangChain.
- **Frontend**: Streamlit for the user interface and Plotly for visualizations.
- **Data Storage**: Pinecone for vector-based document retrieval.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/enterprise-rag-gen-ai.git
   ```

2. Install dependencies:

   ```bash
   pip install -r backend/requirements.txt
   ```

3. Set up your OpenAI and Pinecone API keys in `config/secrets.yaml`.

4. Run the app:

   ```bash
   streamlit run frontend/app.py
   ```

## Running Tests
To run the unit tests for the backend and frontend components, use:

```bash
python -m unittest discover tests
```
