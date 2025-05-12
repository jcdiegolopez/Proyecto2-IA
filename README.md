
# 📚 Asistente de Consulta Técnica con OpenAI y Pinecone

Este proyecto es un asistente inteligente que permite responder preguntas técnicas basándose en documentos PDF cargados por el usuario. Utiliza tecnologías como LangChain, Pinecone, OpenAI y Streamlit para crear una interfaz interactiva de consulta.

----------

## ✅ Instrucciones para la Ejecución

1.  **Clona el repositorio:**
    
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    
    ```
    
2.  **Instala las dependencias necesarias:**
    
    ```bash
    pip install -r requirements.txt
    
    ```
    
3.  **Configura las variables de entorno:**
    
    Crea un archivo `.env` en la raíz del proyecto con las siguientes claves:
    
    ```env
    OPENAI_API_KEY=tu_clave_openai
    PINECONE_API_KEY=tu_clave_pinecone
    
    ```
    
4.  **Agrega documentos PDF:**
    
    Coloca tus archivos `.pdf` en la carpeta `./documents/`.
    
5.  **Ejecuta la aplicación:**
    
    ```bash
    streamlit run main.py
    
    ```
    

----------

## 🧰 Descripción de los Módulos del Proyecto

### 1. `config.py`

-   Carga las claves de API desde el archivo `.env`.
    
-   Asegura que las claves necesarias estén presentes.
    

### 2. `document_loader.py`

-   Carga todos los PDFs de la carpeta `./documents/`.
    
-   Divide los textos en fragmentos de 1000 caracteres usando `RecursiveCharacterTextSplitter`.
    
-   Almacena los vectores en Pinecone para su posterior consulta.
    

### 3. `pinecone_utils.py`

-   Inicializa Pinecone y crea el índice si no existe.
    
-   Establece la conexión con la base de vectores.
    
-   Obtiene el número de vectores almacenados.
    

### 4. `query_processor.py`

-   Realiza búsquedas por similitud sobre los vectores en Pinecone.
    
-   Usa `OpenAI` para generar respuestas basadas en los fragmentos más relevantes.
    

### 5. `main.py` (Aplicación Streamlit)

-   Interfaz gráfica para interacción con el asistente.
    
-   Muestra el estado de carga de documentos y fragmentos.
    
-   Permite al usuario hacer preguntas y ver las respuestas con su contexto.
    

----------

## 🧠 ¿Qué Aprendimos?

### Por Equipo:

-   **Integración de herramientas modernas:** Aprendimos a combinar varias librerías como LangChain, Pinecone, OpenAI y Streamlit para crear una solución robusta.
    
-   **Procesamiento de lenguaje natural:** Comprendimos cómo funcionan los embeddings y la búsqueda semántica para recuperar información relevante.
    
-   **Trabajo colaborativo:** Coordinamos responsabilidades de manera efectiva, organizando los módulos por funcionalidades.
    

### Individualmente:

-   **Nicole Rivera:** Profundicé en el uso de Pinecone y entendí cómo escalar búsquedas vectoriales.
    
-   **Diego Lopez:** Me encargué del manejo de errores y procesamiento de documentos, aprendiendo a lidiar con formatos y errores comunes en PDF. Trabajé en la interfaz con Streamlit y aprendí a diseñar aplicaciones web interactivas con retroalimentación clara para el usuario.
    

----------

## 📂 Estructura del Proyecto

```
├── documents/
│   └── *.pdf
├── modulos/
│   ├── config.py
│   ├── document_loader.py
│   ├── pinecone_utils.py
│   └── query_processor.py
├── main.py
├── requirements.txt
└── .env

