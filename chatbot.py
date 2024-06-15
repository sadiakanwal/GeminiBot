from itertools import zip_longest
import streamlit as st
from streamlit_chat import message
# from langchain.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import ( 
    SystemMessage, HumanMessage, AIMessage)


api_key = st.secrets["API_KEY"]

# Streamit Configuration
st.set_page_config(page_title= "Chat_Model")


# intializing chatModel 
# chat = ChatOpenAI(temperature= 0.5, model_name=" Text" , max_tokens = 100, openai_api_key =api_key)
chat = ChatGoogleGenerativeAI(model="gemini-1.5-flash" , google_api_key= api_key)
#  intiallize session in streamlit
if 'prompt' not in st.session_state:
    st.session_state['prompt'] = ""
if 'response' not in st.session_state:
    st.session_state['response'] = []
if 'input_history' not in st.session_state:
    st.session_state['input_history'] = []

# On Submission of text input
def submit():
    st.session_state.prompt= st.session_state.input
    st.session_state.input=" "


# Layout of CHATBOT___________________________________________

# Sidebar for the text input
st.sidebar.title("INTRODUCTION")




st.sidebar.markdown( "YOUR AI MENTOR IS HERE. You can Ask any question. Just type below and press Enter. ")

# Main content area

styl = f"""
<style>
    .stTextInput {{
      position: fixed;
      bottom: 3rem;
      z-index:1000;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

# Text input for user
st.text_input('user: ' , key= 'input' , on_change= submit)


# --------------------------------------------------------------





# Keep record of Prompts by making lists
def MakingLists():

    Message  = [SystemMessage(content="You are a helpful AI assistant talking with a human. If you do not know an answer, just say 'I don't know', do not make up an answer.")] 

    for userinput, response in zip_longest(st.session_state['input_history'] , st.session_state['response']):
        if userinput is not None:
            Message.append(HumanMessage(content = userinput))
        if response is not None:
            Message.append(AIMessage(content=response))
    return Message





def generate_response():

    message= MakingLists()
    Response= chat(message)
    response = Response.content
    return response

if st.session_state['prompt'] != "":
    userquery = st.session_state['prompt']
    st.session_state.input_history.append(userquery)
    output= generate_response()
    st.session_state.response.append(output)



# Display the chat input_history
if st.session_state['response']:
    for i in range(len(st.session_state['response'])):
        # Display user message
        message(st.session_state['input_history'][i], is_user=True, key=str(i) + '_user')
        # Display AI response
        message(st.session_state["response"][i], key=str(i))
