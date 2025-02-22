# Imports
import streamlit as st
from dotenv import load_dotenv
from mistralai import Mistral
import random

load_dotenv()

import os
# page config
st.set_page_config(page_title='BiryaniGPT', layout='centered',page_icon='🍛')

def randomEmoji () :
   ranEmojiList = ['🥨','🍣','🌭','🥓','🍗','🍜','🥙','🥡','🍕','🍝','🍳']
   return random.choice(ranEmojiList)
#  Main fn
def main (userInput):
   
   ranEmojiUser = randomEmoji()
   with st.chat_message("user",avatar=ranEmojiUser):
      st.write(userInput)
      
   st.session_state.messages.append({"role":"human","avatar":ranEmojiUser,"content":userInput})
   
   with st.chat_message("assistant",avatar='🍛'):
      with st.spinner('hmm...',show_time=True):
         agent_id = os.getenv('agent_id')
         api_key = os.getenv('api_key')
         model = 'mistral-large-2411'
         client =  Mistral(api_key=api_key)
         ai_response = client.agents.complete(
            agent_id = agent_id,
               messages = [
                  {
                     "role":"user",
                     "content" : userInput
                  }
               ]
         )
      st.write(ai_response.choices[0].message.content)
      st.session_state.messages.append({"role":"ai","avatar":"🍛","content":ai_response.choices[0].message.content})
      
# CSS
css="""
<style>
    .title {
        text-align: center;
        background: linear-gradient(90deg, rgb(255, 201, 100), rgb(255, 102, 0), rgb(235, 201, 10));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2rem;
        margin-bottom: 1px;
    }
    
    .subtext {
        color: grey;
        text-align: center;
        font-size: 1rem;
        margin-top: 0;
    }
</style>

     """
     
st.markdown(css,unsafe_allow_html=True)

st.markdown('<h1 class="title">BiryaniGPT</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtext">Spicing Up Conversations, One Byte at a Time</p>', unsafe_allow_html=True)

# chat history iniiaized
if "messages" not in st.session_state:
   st.toast("Hey there! Welcome to BiryaniGPT!🍛✨ Designed to help in kitchen. 💗") 
   st.session_state.messages = []
   st.session_state.input = 'Hi, How are you? 😊'
   st.markdown("<div style='height: 25vh'></div>", unsafe_allow_html=True)
  
# display chat
for message in st.session_state.messages:
   with st.chat_message(message["role"],avatar=message["avatar"]):
      st.text(message["content"])
      
#  react to user input
if userInput := st.chat_input('Spice It Up 🌶 .........'):
   st.session_state.input=userInput

if userInput != '':
   main(userInput=st.session_state.input)