from dotenv import load_dotenv
import os

def load_config():
    load_dotenv()
    config = {
        'openai_api_key': os.getenv('OPENAI_API_KEY'),
        'pinecone_api_key': os.getenv('PINECONE_API_KEY')
    }
    if not all(config.values()):
        raise ValueError("Faltan claves en .env: OPENAI_API_KEY o PINECONE_API_KEY")
    return config