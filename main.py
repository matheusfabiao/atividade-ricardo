import streamlit as st
from langchain.chains import RetrievalQA
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

from config import *

from vectorstore import create_vector_store


# load_dotenv()

st.set_page_config(
    'Assistente de IA',
    page_icon='🤖',
    layout='centered',
    initial_sidebar_state='collapsed',
)

st.title("📄 Chat com PDF usando RAG e IA Generativa")

pdf_files = st.file_uploader(
    "Envie um PDF para começar", type=["pdf"], accept_multiple_files=True
)

if pdf_files:
    
    vectorstore = create_vector_store(pdf_files)
    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

    llm = ChatOpenAI(
        temperature=0, model=OPENROUTER_MODEL, api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_BASE_URL
    )
    
    print('MODELO USADO:', llm.model_name)
    
    rag_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    human_message = st.chat_input('Digite sua mensagem aqui...')

    if 'chats' not in st.session_state:
        st.session_state.chats = []

    if human_message:

        st.session_state.chats.append({'role': 'user', 'content': human_message})

        response = rag_chain.invoke(human_message).get('result')

        st.session_state.chats.append({'role': 'assistant', 'content': response})

    for chat in st.session_state.chats:
        st.chat_message(chat['role']).markdown(chat['content'])
