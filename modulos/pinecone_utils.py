from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import Pinecone as PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
import time
import os

def initialize_pinecone(api_key):
    pc = Pinecone(api_key=api_key)
    index_name = 'technical-query-assistant'
    if index_name not in pc.list_indexes().names():
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric='cosine',
            spec=ServerlessSpec(cloud='aws', region='us-east-1')
        )
        time.sleep(30)  
    return pc, index_name

def get_vectorstore(index_name, openai_api_key):
    embeddings = OpenAIEmbeddings(api_key=openai_api_key)
    pc = Pinecone(api_key=os.getenv('PINECONE_API_KEY'))
    index = pc.Index(index_name)
    return PineconeVectorStore(index=index, embedding=embeddings, text_key="text", namespace='')

def get_vector_count(pc, index_name):
    index = pc.Index(index_name)
    stats = index.describe_index_stats()
    return stats.get('namespaces', {}).get('', {}).get('vector_count', 0)