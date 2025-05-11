from langchain_openai import OpenAI
from langchain.chains.question_answering import load_qa_chain

def process_query(vectorstore, question, openai_api_key):
    docs = vectorstore.similarity_search(question, k=3, namespace='')
    if docs:
        chain = load_qa_chain(OpenAI(api_key=openai_api_key), chain_type="stuff")
        answer = chain.run(input_documents=docs, question=question)
        return answer, docs
    return None, []