from metallma2wambugu.huglogin import login
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.document_loaders import TextLoader
#from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceHubEmbeddings
from langchain.llms.base import LLM
from langchain.chains import RetrievalQA
import warnings
import random
import string
import sys
from hugchat import hugchat
from hugchat.login import Login
import os
import time
from custom_hugchat import custom_chat #email, password 
from answer_pdf import question_pdf #llm, text, prompt
from pdf_reader import read_pdf #obj.read("filename.pdf")
import streamlit as st
#import logging
#logging.basicConfig(level=logging.DEBUG)
HUGGINGFACEHUB_API_TOKEN= os.environ["HUGGINGFACEHUB_API_TOKEN"] 
REPO_ID  = "sentence-transformers/all-mpnet-base-v2"
email= os.environ["EMAIL"]
psw = os.environ["PASS"]

@st.cache_data
def chatwithme():
    email= os.environ["EMAIL"]
    pass_w = os.environ["PASS"]
        #chatbot = login(email,pass_w).login()
    sign = Login(email,pass_w)
    cookies = sign.login()
    
    # Save cookies to the local directory
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())#.query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)
    return chatbot
def web_res(res):
    new = [f" - __Source from the web:__ - `Title`:{source.title} - `source`: {source.hostname}  `Link`: {source.link}" for source in res.web_search_sources]
    return new
      

@st.cache_data
def llama_llm(email:str, psw:str):
    llm = custom_chat(email= email, psw= psw)
    return llm
      

               # st.markdown("### Sources on the web:")
                
st.header("Meta llama2-70b Chat")

with st.sidebar:
    st.subheader("Web search")
    websearch=st.checkbox("Web search?")
    st.header("QA with your pdf")
    quiz_ans = st.checkbox("Question and answer?")
    if quiz_ans ==True:
        uploaded = st.file_uploader('Choose your .pdf file', type="pdf")
        if uploaded is not None:
            text_ = read_pdf.read(uploaded)

    
    st.markdown("__Developer:__ Wambugu kinyua")
    
    st.markdown("__Email:__ kenliz1738@gmail.com")
    st.markdown("The app is still in development it might break")
    
st.markdown(" `Dev k. WAMBUGU` ")
from streamlit_custom_notification_box import custom_notification_box
styles = {'material-icons':{'color': 'red'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 8px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}


try:
    
    #if websearch:
     #   st.markdown("Web search enabled")
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("Ask your question?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)
    
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                message_placeholder = st.empty()
                full_response = ""
                assistant_response = chatwithme().query(prompt,temperature= 0.5, max_new_tokens= 4029)['text']#chatbot.chat(prompt)['text']
                # Simulate stream of response with milliseconds delay
                #with st.spinner(text="Generating response..."):
               #### for chunk in assistant_response.split():
                    ###full_response += chunk + " "
                   ### time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                    
                if websearch ==False and quiz_ans == False:
                    message_placeholder.markdown(assistant_response)# + "▌")
                if websearch== True and quiz_ans == False:
                    data = chatwithme().query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)['text']
                    assistant_response = data['text'] + ' '.join(web_res(data))
                    message_placeholder.markdown(assistant_response)
                if websearch == False and quiz_ans== True:
                    assistant_response =question_pdf(llama_llm(email, psw),text_, prompt)
                    message_placeholder.markdown(assistant_response)
                
         ######
         #####
         ###       assistant_response = 

            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
           # st.session_state.messages.append()
        ####
except:
   # custom_notification_box(icon='info', textDisplay='Server error, try reprompting again', styles=styles, key ="foo")
    custom_notification_box(icon='info', textDisplay='Server error, try reprompting again...', externalLink='more info', url='#', styles=styles, key="foo")
# Initialize chat history
