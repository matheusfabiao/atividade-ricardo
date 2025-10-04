import os

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


def __process_file(pdf_files):
    os.makedirs("docs", exist_ok=True)
    all_docs = []
    for pdf_file in pdf_files:
        file_path = f"docs/{pdf_file.name}"
        with open(file_path, "wb") as f:
            f.write(pdf_file.read())

        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)
    return all_docs


def __chunk_splitting(pdf_file):
    docs = __process_file(pdf_file)
    splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(docs)


def create_vector_store(pdf_file):
    texts = __chunk_splitting(pdf_file)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_documents(texts, embeddings)
