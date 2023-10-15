from metallma2wambugu.huglogin import login
import sys
from hugchat import hugchat
from hugchat.login import Login
import os
import time
import streamlit as st
#import logging
#logging.basicConfig(level=logging.DEBUG)
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
               # st.markdown("### Sources on the web:")
                
st.header("Meta llama2-70b Chat")
#def webs(res):
 #   for source in res.web_search_sources:
      #  return ### Essential sources on the web: Title: {source.title} Source: {source.hostname} Link: {source.link}"#)
       # message_placeholder.markdown(source.link)
      #  time.sleep(0.005)
    #    st.markdown(f"Title: {source.title}")
    #    time.sleep(0.005)
      #  st.markdown(f"Source: {source.hostname}")
  #      time.sleep(0.005)
     #   st.markdown(f"Link: {source.link}")
#[st.markdown(i) for i in ["Hi😂", 23, 43, "hdhdb😊"]]
with st.sidebar:
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

custom_notification_box(icon='info', textDisplay='😂😂🤠We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
# Initialize chat history
try:
    websearch=st.checkbox("Web search?")
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
                if websearch ==False:
                    message_placeholder.markdown(assistant_response)# + "▌")
                if websearch== True:
                    data = chatwithme().query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)['text']
                    assistant_response = data['text'] + ' '.join(web_res(data))
                    message_placeholder.markdown(assistant_response)
               # message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            #st.markdown(
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
           # st.session_state.messages.append()
        ####
except:
    custom_notification_box(icon='info', textDisplay='Server error, try reprompting again', styles=styles, key ="foo")

