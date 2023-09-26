from metallma2wambugu.huglogin import login
import sys
import os
import time
import streamlit as st
def chatwithme(prompt):
    email= os.environ["EMAIL"]
    pass_w = os.environ["PASS"]
    chatbot = login(email,pass_w).login()
    return chatbot.query(f"{prompt}",temperature= 0.5, max_new_tokens= 4029)['text']#chatbot.chat(prompt)
    
st.title("Meta llama2 70b chat")
with st.sidebar:
    st.markdown("__Developer:__ Wambugu kinyua")
    st.markdown("__Email:__ kenliz1738@gmail.com")
    st.markdown("The app is still in development it might break")
    
st.markdown(" `Dev k. WAMBUGU` ")
# Initialize chat history
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
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = chatwithme(prompt)
        # Simulate stream of response with milliseconds delay
        #with st.spinner(text="Generating response..."):
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.005)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    #st.markdown(
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    ####
