from PyPDF2 import PdfReader
from typing import List, Optional
import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings.openai import OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
import streamlit as st
from htmlreference import css, user, chatbot
from dotenv import load_dotenv


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

def get_text(uploaded_docs):
    """
    Takes in a list of PDF file paths, reads their text, and returns a concatenated string.

    Parameters:
    uploaded_docs (List): A list of file-like objects representing the PDFs.

    Returns:
    str: A string containing all the text extracted from the PDFs.
    """
    content = ""
    for doc in uploaded_docs:
        reader = PdfReader(doc)
        for page in reader.pages:
            content += page.extract_text()
    return content

def get_chunks(text):
    """
    Splits the given text into smaller chunks suitable for processing.

    Parameters:
    text (str): A string of text to be split.

    Returns:
    List[str]: A list of strings, where each is a chunk of the original text.
    """
    splitter = CharacterTextSplitter(
        chunk_size = 1024,
        separator ='\n',
        chunk_overlap = 256,
        length_function = len
    )
    return splitter.split_text(text)

def get_embeddings(chunks):
    """
    Creates vector embeddings for each text chunk and stores them in a FAISS vector store.

    Parameters:
    chunks (List[str]): A list of text chunks to be embedded.

    Returns:
    FAISS: A FAISS vector store containing the vector embeddings of the chunks.
    """
    embeds = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vector_embeddings = FAISS.from_texts(texts = chunks, embedding = embeds)
    return vector_embeddings

def converse(vector_embeddings):
    """
    Sets up and returns a conversational retrieval chain using the provided vector embeddings.

    Parameters:
    vector_embeddings (FAISS): A FAISS vector store containing vector embeddings of text chunks.

    Returns:
    ConversationalRetrievalChain: The initialized conversational retrieval chain.
    """
    model = ChatOpenAI()
    mem = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm = model,
        retriever = vector_embeddings.as_retriever(),
        memory = mem
    )
    return chain

def respond(input):
    """
    Takes user input, generates a response using the conversational chain, and displays the conversation history.

    Parameters:
    input (str): The user input to be processed by the conversational chain.
    """
    if st.session_state.conversation is None:
        st.write("Please upload your document(s) first")
        return
    output = st.session_state.conversation({'question': input})
    st.session_state.history = output['chat_history']

    for x, message in enumerate(st.session_state.history):
        if x %2 == 0:
            st.write(user.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(chatbot.replace("{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    """
    Main function to initialize the Streamlit app.
    """
    load_dotenv()
    st.set_page_config(page_title='PDF Chatbot')

    st.write(css, unsafe_allow_html = True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    
    if "history" not in st.session_state:
        st.session_state.history = None

    st.header('Q&A with Chatbot :file_folder:')

    input = st.text_input('Ask me anything about the PDFs you uploaded')

    if input:
        respond(input)
    with st.sidebar:
        uploaded_docs = st.file_uploader('Click on Add to upload your PDFs', accept_multiple_files=True)
        if st.button('Add'):
            with st.spinner("Adding"):
                text = get_text(uploaded_docs)
                
                chunks = get_chunks(text)

                vector_embeddings = get_embeddings(chunks)

                st.session_state.conversation = converse(vector_embeddings)



if __name__ == '__main__':
    main()