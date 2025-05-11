import streamlit as st
from modulos.config import load_config
from modulos.pinecone_utils import initialize_pinecone, get_vector_count, get_vectorstore
from modulos.document_loader import load_and_process_documents
from modulos.query_processor import process_query


config = load_config()


pc, index_name = initialize_pinecone(config['pinecone_api_key'])
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = get_vectorstore(index_name, config['openai_api_key'])
if 'vector_count' not in st.session_state:
    st.session_state.vector_count = get_vector_count(pc, index_name)
if 'documents_loaded' not in st.session_state:
    st.session_state.documents_loaded = False


if not st.session_state.documents_loaded and st.session_state.vector_count < 70:
    st.session_state.vector_count = load_and_process_documents(st.session_state.vectorstore, pc, index_name)
    st.session_state.documents_loaded = True
    if st.session_state.vector_count >= 70:
        st.success(f"Se cargaron {st.session_state.vector_count} fragmentos. Mínimo de 70 registros alcanzado.")
    else:
        st.error(f"Se cargaron {st.session_state.vector_count} fragmentos. Faltan {70 - st.session_state.vector_count} para alcanzar el mínimo de 70 registros. Agrega más PDFs en ./documents/.")
elif st.session_state.vector_count >= 70:
    st.success(f"Ya existen {st.session_state.vector_count} fragmentos. Mínimo de 70 registros alcanzado.")

st.title('Asistente de Consulta Técnica')


st.write(f"Fragmentos almacenados: {st.session_state.vector_count}/70")

st.header('Hacer una Pregunta')


if st.session_state.vector_count >= 70:
    question = st.text_input("Ingresa tu pregunta")
    if st.button('Obtener Respuesta'):
        answer, contexts = process_query(st.session_state.vectorstore, question, config['openai_api_key'])
        if answer:
            st.write(f"**Respuesta:** {answer}")
            st.subheader("Contexto Utilizado:")
            for i, context in enumerate(contexts, 1):
                st.write(f"**Documento {i}:**")
                st.write(context.page_content)
                st.write("---")
        else:
            st.write("No se encontraron documentos relevantes.")
else:
    st.error("No se han alcanzado los 70 fragmentos mínimos. Agrega más PDFs en ./documents/ y reinicia la aplicación.")