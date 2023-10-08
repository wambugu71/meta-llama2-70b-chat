from metallma2wambugu.huglogin import login
import sys
from hugchat import hugchat
from hugchat.login import Login
import os
import time
import streamlit as st
def chatwithme(prompt):
    email= os.environ["EMAIL"]
    pass_w = os.environ["PASS"]
    #chatbot = login(email,pass_w).login()
    sign = Login(email,pass_w)
    cookies = sign.login()

# Save cookies to the local directory
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    return chatbot.query(prompt,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)
st.title("Meta llama2-70b Chat")
[st.markdown(i) for i in ["Hi😂", 23, 43, "hdhdb😊"])
with st.sidebar:
    st.markdown("__Developer:__ Wambugu kinyua")
    st.markdown("__Email:__ kenliz1738@gmail.com")
    st.markdown("The app is still in development it might break")
    
st.markdown(" `Dev k. WAMBUGU` ")
# Initialize chat history
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
            assistant_response = chatwithme(prompt)['text']
            # Simulate stream of response with milliseconds delay
            #with st.spinner(text="Generating response..."):
           #### for chunk in assistant_response.split():
                ###full_response += chunk + " "
               ### time.sleep(0.05)
                # Add a blinking cursor to simulate typing
            message_placeholder.markdown(assistant_response)# + "▌")
            if websearch:
               # st.markdown("### Sources on the web:")
                for source in chatwithme(prompt).web_search_sources:
                    #time.sleep(0.05)
                    st.markdown("### Essential sources on the web:")
                   # message_placeholder.markdown(source.link)
                    time.sleep(0.005)
                    st.markdown(f"Title: {source.title}")
                    time.sleep(0.005)
                    st.markdown(f"Source: {source.hostname}")
                    time.sleep(0.005)
                    st.markdown(f"Link: {source.link}")
           # message_placeholder.markdown(full_response)
        # Add assistant response to chat history
        #st.markdown(
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})
       # st.session_state.messages.append()
    ####
