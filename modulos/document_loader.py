import time
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
import glob
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_and_process_documents(vectorstore, pc, index_name):
    all_docs = []
    documents_folder = './documents/'
    

    if not os.path.exists(documents_folder):
        os.makedirs(documents_folder)
        logger.warning(f"Carpeta {documents_folder} creada, pero está vacía. Agrega PDFs.")
    
  
    pdf_files = glob.glob(os.path.join(documents_folder, '*.pdf'))
    if not pdf_files:
        logger.error(f"No se encontraron PDFs en {documents_folder}. Agrega archivos PDF válidos.")
        return 0
    
    for pdf_file in pdf_files:
        try:
            logger.info(f"Procesando {pdf_file}")
            loader = PyPDFLoader(pdf_file)
            docs = loader.load()
            all_docs.extend(docs)
        except Exception as e:
            logger.error(f"Error al procesar {pdf_file}: {str(e)}")
            continue


    if all_docs:
        try:
            logger.info(f"Se cargaron {len(all_docs)} documentos. Dividiendo en fragmentos...")
            text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            texts = text_splitter.split_documents(all_docs)
            logger.info(f"Se generaron {len(texts)} fragmentos. Almacenando en Pinecone...")
            vectorstore.add_documents(texts, namespace='')
            index = pc.Index(index_name)
            time.sleep(5) 
            stats = index.describe_index_stats()
            vector_count = stats.get('namespaces', {}).get('', {}).get('vector_count', 0)
            logger.info(f"Total de fragmentos almacenados: {vector_count}")
            return vector_count
        except Exception as e:
            logger.error(f"Error al procesar o almacenar documentos: {str(e)}")
            return 0
    else:
        logger.error("No se cargaron documentos válidos. Verifica los PDFs.")
        return 0