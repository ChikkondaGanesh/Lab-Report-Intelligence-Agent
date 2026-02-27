import os
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load ONLY text files (no unstructured dependency)
loader = DirectoryLoader(
    "knowledge",
    glob="**/*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)

# Load embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS index
vectorstore = FAISS.from_documents(docs, embedding_model)

# Save index
vectorstore.save_local("rag/vector_db")

print("✅ Vector DB Created Successfully!")