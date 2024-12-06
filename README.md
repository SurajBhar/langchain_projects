# LangChain Projects

Welcome to the **LangChain Projects** repository! 🎉

This repository is dedicated to tutorials and practical examples for working with LangChain, Retrieval-Augmented Generation (RAG), and Vector Databases. Whether you're a beginner or an experienced practitioner, you'll find valuable resources to enhance your understanding of these powerful tools for building advanced AI applications.

---

## 📚 Tutorials Covered

### 1. **LangChain Introduction**
   - Overview of LangChain and its core concepts.
   - Understanding the building blocks like chains, agents, and tools.
   - Getting started with your first LangChain project.

### 2. **Data Ingestion through LangChain Document Loaders**
   - How to load and process data using LangChain's document loaders.
   - Supported formats and integration with various data sources.
   - Practical examples for loading PDFs, text files, and more.

### 3. **Data Transformation Using Text Splitting**
   - Techniques for efficient data transformation.
   - Splitting large documents into manageable chunks for downstream processing.
   - Practical examples using LangChain's text splitting utilities.

### 4. **Embeddings Generation**
   - Generating embeddings for your data using:
     - **OpenAI** models
     - **Ollama** models
     - **Hugging Face** models
   - Understanding embedding quality and applications.

### 5. **Vector Stores: FAISS and ChromaDB**
   - Storing and querying embeddings efficiently.
   - Hands-on tutorials for:
     - **FAISS**: Scalable similarity search.
     - **ChromaDB**: Flexible vector database.
   - Building RAG workflows using these vector stores.

---

## 🚀 Why LangChain, RAG, and Vector Databases?

- **LangChain**: A framework to build powerful AI applications by chaining together LLMs, tools, and APIs.
- **RAG (Retrieval-Augmented Generation)**: Combines retrieval systems with language models for grounded and accurate AI outputs.
- **Vector Databases**: Enable fast and scalable similarity search for embeddings, empowering applications like semantic search and recommendation systems.

---

## 🛠 Prerequisites

Before diving into the tutorials, ensure you have the following installed:

- Python 3.8 or higher
- Required libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

---

## 🚀 Clone the Repostiroy:
- Clone the repository using following command:
```
git clone https://github.com/SurajBhar/langchain_projects.git

```
- Navigate to the desired tutorial folder.
- Follow the instructions in each tutorial to get started.

---

## 🚀 Repostiroy Structure:
```
langchain_projects/
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── L1_Langchain/
│   ├── 1_1_openai/GettingStarted.ipynb # Introduction to LangChain
│   ├── 1_2_Data_ingestion/langchain_data_ingestion.ipynb         # Document loaders tutorial
│   ├── 1_3_Text_Splitting/       # Data transformation examples
│   │        ├── text_splitting.ipynb # Introduction to text splitting
│   │        ├── html_header_text_splitter.ipynb # HTML Text Splitting
│   │        ├── json_data_splitting.ipynb # Json data Splitting
├── L2_Embeddings/
│   ├── L2_1_openai/       # Openai for embeddings
│   │        ├── openai_embeddings.ipynb
│   ├── L2_2_Ollama/       # Ollama for embeddings
│   │        ├── ollama_embeddings.ipynb
│   ├── L2_3_Hugging_Face/       # Hugging Face for Embeddings
│   │        ├── embed_hugging_face.ipynb
├── L3_VectorStore/
│   ├── L3_1_FAISS/       # FAISS Library for Vector Stores
│   │        ├── faiss.ipynb
│   ├── L3_2_ChromaDB/       # ChromaDB VectorStore
│   │        ├── chroma.ipynb
```
---

## 🤝 Contributing
Contributions are welcome! If you have ideas, bug fixes, or enhancements, feel free to open an issue or submit a pull request.

---

## 💡 Resources
- LangChain Documentation : https://python.langchain.com/docs/integrations/document_loaders/
- OpenAI : https://platform.openai.com/docs/overview
- Hugging Face : https://huggingface.co/
- FAISS : https://faiss.ai/index.html
- ChromaDB : https://docs.trychroma.com/
- Ollama : https://ollama.com/blog

---