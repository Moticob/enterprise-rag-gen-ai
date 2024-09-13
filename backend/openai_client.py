import openai
import yaml

class OpenAIClient:
    def __init__(self):
        # Load API Key from secrets.yaml
        with open("config/secrets.yaml", "r") as f:
            secrets = yaml.safe_load(f)
        
        self.api_key = secrets['openai_api_key']
        openai.api_key = self.api_key

    def get_llm(self):
        # Set up LLM (GPT-4) for LangChain integration
        from langchain.llms import OpenAI
        llm = OpenAI(model_name="gpt-4", openai_api_key=self.api_key)
        return llm

    def generate_response(self, prompt):
        # Generate a response using GPT-4
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()

