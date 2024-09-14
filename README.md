# Enterprise RAG - Transform Business Process & Decision-Making with Generative AI

![OpenAI Logo](https://upload.wikimedia.org/wikipedia/commons/4/4f/OpenAI_Logo.png)
![Pinecone Logo](https://upload.wikimedia.org/wikipedia/commons/6/6e/Pinecone_Logo.png)
![Streamlit Logo](https://upload.wikimedia.org/wikipedia/commons/0/05/Streamlit_Logo.png)

## Repository Name: `enterprise-rag-gen-ai`

## Project Structure:
```bash
enterprise-rag-gen-ai/
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── rag_engine.py
│   ├── pinecone_client.py
│   ├── openai_client.py
│   └── requirements.txt
├── frontend/
│   ├── __init__.py
│   ├── app.py
│   └── assets/
│       ├── styles.css
│       └── logo.png
├── config/
│   ├── config.yaml
│   ├── secrets.yaml
├── data/
│   └── sample_data.json
├── tests/
│   ├── test_rag_engine.py
│   ├── test_openai_client.py
│   ├── test_pinecone_client.py
│   └── test_app.py
├── docs/
│   ├── README.md
│   ├── INSTALLATION.md
│   ├── WORKFLOW.md
│   └── PRESENTATION.pptx
├── .gitignore
├── README.md
├── LICENSE
└── Dockerfile
```

## Explanation of Each Folder and Files:

### 1. Backend Folder: `backend/`
This folder contains all the backend code, including the core logic for interacting with GPT-4 (OpenAI), the Retrieval-Augmented Generation (RAG) engine, and Pinecone.

- `main.py`: Entry point for running the backend services, including the initialization of the RAG engine.
- `rag_engine.py`: Implements the core logic of the Retrieval-Augmented Generation (RAG) system using LangChain, OpenAI GPT-4, and Pinecone.
- `pinecone_client.py`: Contains logic to interact with Pinecone, including initializing the Pinecone database, storing, and retrieving vectorized business data.
- `openai_client.py`: Handles interaction with OpenAI’s GPT-4 API, sending queries, and receiving responses.
- `requirements.txt`: Lists the dependencies required for the backend code.

```plaintext
openai
pinecone-client
langchain
streamlit
plotly
pyyaml
```

### 2. Frontend Folder: `frontend/`
This folder contains all the files required for the user interface, including the Streamlit app for the interactive Q&A and the dashboard.

- `app.py`: Main file for the Streamlit app, handling the user interface for the Q&A system, visualizations, and interaction with the backend API.
- `assets/`: Stores static assets for the frontend like custom stylesheets or images.
   - `styles.css`: Custom CSS to improve the look of the Streamlit interface.
   - `logo.png`: Placeholder logo image for branding the UI.

### 3. Config Folder: `config/`
This folder holds configuration files for environment settings and API credentials.

- `config.yaml`: General configuration file for settings like Pinecone index, OpenAI model type, etc.
- `secrets.yaml`: Stores sensitive API keys for Pinecone and OpenAI. This file should be added to `.gitignore`.

### 4. Data Folder: `data/`
This folder stores any business-related data or sample datasets used for testing and demo purposes.

- `sample_data.json`: A sample JSON file for simulating business data to showcase the RAG engine.

### 5. Tests Folder: `tests/`
This folder contains unit and integration tests for the different modules.

- `test_rag_engine.py`: Tests the functionality of the RAG engine.
- `test_openai_client.py`: Ensures that interactions with the OpenAI API are working properly.
- `test_pinecone_client.py`: Tests Pinecone vector operations (storing, retrieving).
- `test_app.py`: Tests the frontend functionality.

### 6. Docs Folder: `docs/`
This folder contains all documentation related to the project, including setup instructions, workflow descriptions, and presentation materials.

- `README.md`: Main readme file explaining the project, its objectives, and how to set it up.
- `INSTALLATION.md`: Detailed installation guide.
- `WORKFLOW.md`: Explains how each part of the system works.
- `PRESENTATION.pptx`: Presentation slides summarizing the project.

### 7. Other Files:
- `.gitignore`: Specifies which files and folders should not be included in the Git repository.

```plaintext
config/secrets.yaml
.env
venv/
__pycache__/
*.pyc
```

- `README.md`: Brief explanation of the project, including its purpose, tech stack, and high-level overview.

```markdown
# Enterprise RAG Gen AI

This project aims to revolutionize business decision-making by leveraging Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to provide real-time, actionable insights.

## Features:
- Gen AI-powered decision engine using GPT-4.
- Real-time retrieval of company-specific data using Pinecone.
- Interactive Q&A system for business strategies.

## Tech Stack:
- Python, Streamlit, Pinecone, OpenAI API, LangChain.

## Quick Start:
- Install dependencies using `pip install -r backend/requirements.txt`.
- Set up your API keys in `config/secrets.yaml`.
- Run the frontend using `streamlit run frontend/app.py`.
```

- `LICENSE`: Choose an open-source license (e.g., MIT) to allow others to use or modify the code.
- `Dockerfile`: To containerize the application for easy deployment.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install the necessary dependencies
RUN pip install -r backend/requirements.txt

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define the environment variable
ENV STREAMLIT_SERVER_PORT 8501

# Run the Streamlit app
CMD ["streamlit", "run", "frontend/app.py"]
```

## Detailed Flow of the Project:

### Backend Setup:
- `backend/main.py`: Initialize the RAG engine.
- `backend/rag_engine.py`: Query Pinecone for relevant documents and feed them into GPT-4 for strategy generation.
- `backend/pinecone_client.py`: Manage interactions with the Pinecone vector database (store/retrieve vectors).
- `backend/openai_client.py`: Handle the GPT-4 API for language generation and insights.

### Frontend:
- `frontend/app.py`: A simple Streamlit app where users can ask business-related questions and see real-time insights and data visualizations.
- `frontend/assets/`: Store any custom styles or images for branding.

### Config:
- `config/config.yaml` and `secrets.yaml`: Manage API keys and configuration settings.

### Testing:
- Unit tests for each part of the backend to ensure everything is working as expected.

### Documentation:
- Include detailed project documentation and presentations explaining the process and benefits of the system.

### Deployment:
- The Dockerfile will allow easy deployment of the project on cloud platforms.
