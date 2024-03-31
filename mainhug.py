import streamlit as st
from hugchat import hugchat
import  os
from hugchat.login import Login
st.set_page_config(layout = "wide", page_title  = "OmniHelper", initial_sidebar_state="expanded", page_icon = "logo_trial.png")
email= os.environ["EMAIL"] 
pass_w = os.environ["PASS"]
@st.cache_resource(show_spinner="Loading the model")#(experimental_allow_widgets=True)
def chatwithme(model, sysprompt):
    email= os.environ["EMAIL"] 
    pass_w = os.environ["PASS"] 
    global chatbot
        #chatbot = login(email,pass_w).login()
    sign = Login(email,pass_w)
    cookies = sign.login()
    
    # Save cookies to the local directory
    cookie_path_dir = "./cookies_snapshot"
    sign.saveCookiesToDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
#,temperature= 0.5, max_new_tokens= 4029, web_search=True)#chatbot.chat(prompt)
    chatbot.switch_llm(model)
    chatbot.new_conversation(switch_to =True, system_prompt=f"Your name is 'Wambugu kinyua AI' assistant,your role is : '+ {sysprompt}")
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

st.header("OmniHelper")
@st.cache_resource(show_spinner=False)
def web_search(prompt):
    cookie_path_dir = "./cookies_snapshot1"
    sign = Login(os.environ['EMAIL'], os.environ['PASS'])
    cookies = sign.login()#cookies = sign.loadCookiesFromDir(cookie_path_dir)
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    res = chatbot.query(prompt, temperature=0.6, web_search=True)
    yield res['text']
    new = [f" - __Link from the web: `Link`: {source.link}" for source in res.web_search_sources]
    yield  "{}".format(' '.join(new))
    #return full_resp

with st.sidebar:
    with st.expander("Realtime  results", expanded =False):
        st.markdown("Access real time response:")
        websearch = st.checkbox("Web search")

def clear():
    st.cache_resource.clear()
@st.cache_data(show_spinner= False)
def  chat_models():
    cookie_path_dir = "./cookies_snapshot1"
    sign = Login(os.environ['EMAIL'], os.environ['PASS'])
    cookies = sign.login()#cookies = sign.loadCookiesFromDir(cookie_path_dir)
    chat = hugchat.ChatBot(cookies=cookies.get_dict())
    return chat.get_available_llm_models()
    
with st.sidebar:   
    models = chat_models()
    models_all = [i.name for i in  models]
    with st.container(border=True, height =100):
        option = st.radio('Choose your preferred model:',models_all,on_change=clear)
    syspromptfromuser = st.text_area(label = "System prompt",
    placeholder = "Define  what role should  it  do or expert in what 'field'.",
    )
    st.markdown("__Developer:__ Wambugu kinyua")
    st.markdown("__Email:__ kenliz1738@gmail.com")
    st.markdown("__Note:__ The app is still in development it might break")
    try:
        idx = models_all.index(option)
        mychatbot = chatwithme(idx,syspromptfromuser )
    except ValueError as e:
        print("Desired modelnot  found.")
        idx = 0
        mychatbot = chatwithme(idx, syspromptfromuser)
#st.title("Ai Hub")
def  st_ream(prompt, chatbot):
    for resp in chatbot.query(
        prompt,
        stream=True
    ):
        try:
            yield resp['token']
        except:
            pass

        
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask your query"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        #if  prompt != None:
        if  websearch:
            with st.spinner("Searching for  your query..."):
                response = st.write_stream( web_search(prompt))
        else:
            response = st.write_stream(st_ream(prompt, mychatbot))
        
    st.session_state.messages.append({"role": "assistant", "content": response})
