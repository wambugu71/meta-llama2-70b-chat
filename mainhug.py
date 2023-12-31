#from metallma2wambugu.huglogin import login
#import sys
from hugchat import hugchat
from hugchat.login import Login
import os
import time
from functools import lru_cache
import streamlit as st
#import logging
#logging.basicConfig(level=logging.DEBUG)
@st.cache_resource(show_spinner="Loading the model")#(experimental_allow_widgets=True)
def chatwithme(model):
    email= os.environ["EMAIL"]
    pass_w = os.environ["PASS"]
        #chatbot = login(email,pass_w).login()
    sign = Login(email,pass_w)
    cookies = sign.login()
    
    # Save cookies to the local directory
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
#,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)
    chatbot.switch_llm(model)
    chatbot.new_conversation(switch_to =True, system_prompt="Your name is 'Wambugu kinyua AI', If you are greeted with hello, hey, how are you, etc your reply must have  'Hello welcome to Wambugu kinyua AI assistant, ask anything...'")
    return chatbot
   # if os.environ["EMAIL"] or os.environ["PASS"] ==None:
   #     st.error("Huggingface Login required!")
logo = """ <header>
  <div class="container">
    <h1 class="logo"><a href="#">AI HUB</a></h1>
  </div>
</header>

<style>
  body {
  font-family: Arial, sans-serif;
}

header {
  background-color: #3498db;
  padding: 20px;
  color: white;
  text-align: center;
}

.container {
  max-width: 1200px;
  margin: auto;
}

.logo {
  float: left;
  font-size: 24px;
  line-height: 60px;
}

.logo a {
  color: inherit;
  text-decoration: none;
}

nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
}

nav li {
  float: right;
}

nav a {
  display: block;
  padding: 10px 20px;
  color: white;
  text-decoration: none;
}

nav a:hover {
  background-color: #ddd;
  color: black;
}
</style>
"""
#@st.cache_resource
def login_data():
    
    return cookies
    
st.header("AI-Hub")

def web_search(prompt):
    sign = Login(os.environ['EMAIL'], os.environ['PASS'])
    cookies = sign.login()
    cookie_path_dir = "./cookies_snapshot1"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    res = chatbot.query(prompt, temperature=0.6, web_search=True)
    new = [f" - __Source from the web:__ - `Title`:{source.title} - `source`: {source.hostname}  `Link`: {source.link}" for source in res.web_search_sources]
    full_resp = "{} {}".format(res["text"],' '.join(new))
    return full_resp
               # st.markdown("### Sources on the web:")
#chatbot = hugchat.ChatBot(cookies=chatwithme().get_dict())#.query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)
   # return chatbot

#st.markdown("")

#websearch: bool = False #to a void an error.

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

with st.sidebar:
    st.markdown("Access real time response:")
    websearch = st.checkbox("Web search")
    st.markdown("__Developer:__ Wambugu kinyua")
    st.markdown("__Email:__ kenliz1738@gmail.com")
    st.markdown("__Note:__ The app is still in development it might break")
#option_label=False
#on = st.toggle("Enable model switching:")
#if on:
#    st.cache_data.clear()
def clear():
    st.cache_resource.clear()
    
option = st.selectbox('Choose your preferred model:',('Llama-2-70b-chat-hf', 'CodeLlama-34b-Instruct-hf', 'falcon-180B-chat', 'Mistral-7B-Instruct-v0.1'),on_change=clear)
st.markdown(f'- You selected: _{option}_')
if option == 'Llama-2-70b-chat-hf':
    
    chatbot = chatwithme(0)
    #chatbot.new_conversation(switch_to =True)
    #chatbot = chatwithme(0)#new_conversation(switch_to =True)
elif option == "CodeLlama-34b-Instruct-hf":
   # st.cache_data.clear()
    chatbot  = chatwithme(1)
   # chatbot.new_conversation(switch_to =True)#chatbot = chatwithme(1)#chatbot.switch_llm(1)
    #chatbot.new_conversation(switch_to =True)
elif option == "falcon-180B-chat":
    #st.cache_data.clear()
    chatbot  = chatwithme(2)
   # chatbot.new_conversation(switch_to =True)#chatbot = chatwithme(2)#chatbot.switch_llm(2)
    #chatbot.new_conversation(switch_to =True)
elif option == "Mistral-7B-Instruct-v0.1":
    #st.cache_data.clear()
    chatbot  = chatwithme(3)
   # chatbot.new_conversation(switch_to =True)#chatbot = chatwithme(3)#chatbot.switch_llm(3)
    #chatbot.new_conversation(switch_to =True)
else:
    st.markdown("Model not available!")
#.query(prompt
st.markdown(" `Dev k. WAMBUGU` ")

from streamlit_custom_notification_box import custom_notification_box
styles = {'material-icons':{'color': 'red'},
          'text-icon-link-close-container': {'box-shadow': '#3896de 0px 8px'},
          'notification-text': {'':''},
          'close-button':{'':''},
          'link':{'':''}}

#custom_notification_box(icon='info', textDisplay='😂😂🤠We are almost done with your registration...', externalLink='more info', url='#', styles=styles, key="foo")
# Initialize chat history
try:
#    websearch=st.checkbox("Web search?")
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
                assistant_response = chatbot.query(prompt,temperature= 0.5, max_new_tokens= 4029)['text']#chatbot.chat(prompt)['text']
                # Simulate stream of response with milliseconds delay
                #with st.spinner(text="Generating response..."):
               #### for chunk in assistant_response.split():
                    ###full_response += chunk + " "
                   ### time.sleep(0.05)
                    # Add a blinking cursor to simulate typing
                if websearch ==False:
                    message_placeholder.markdown(assistant_response)# + "▌")
                if websearch== True:
                   # data = chatbot.query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)['text']
                    assistant_response = web_search(prompt)
                    message_placeholder.markdown(assistant_response)
               # message_placeholder.markdown(full_response)
            # Add assistant response to chat history
            #st.markdown(
            st.session_state.messages.append({"role": "assistant", "content": assistant_response})
           # st.session_state.messages.append()
        ####
except:
   # custom_notification_box(icon='info', textDisplay='Server error, try reprompting again', styles=styles, key ="foo")
    st.error("server error handling your result, reprompt again")#(icon='info', textDisplay='Server error, try reprompting again...', externalLink='more info', url='#', styles=styles, key="foo")
# Initialize chat history
