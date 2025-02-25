import streamlit as st

with st.sidebar:
    st.set_page_config(page_title="Experimental RAG with LLM", page_icon=":robot:")
    st.header("RAG Q&A with MISTRAL 5B Model")
    uploaded_file = st.file_uploader("Upload a PDF", type="pdf", accept_multiple_files=False)
    
    process = st.button("Process")
    
        