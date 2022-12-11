import streamlit as st
import os
import openai
import random
import time

st.set_page_config(page_title="Jarvis AI", page_icon=":tada:")
#st.set_option("font-family","Playfair Display")

page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1525548002014-e18135d814d7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80");
opacity: 0.9;

}
[data-testid="stMarkdownContainer"]{
font-family: "Playfair Display"
}
</style>
"""


st.markdown(page_bg_img,unsafe_allow_html=True)
notif = ["Hang tight...", "Initializing...", "Almost there...", "Hang on...", "Loading...", "Give me a minute...", "Finding an answer...", "Thinking...."]
with st.container():
    st.header("Welcome to a new world of creativity. :wave:")
    st.subheader("Meet Jarvis. An intelligent assistant using OpenAI.")
    st.write("You can ask Jarvis to answer questions, write a paragraph, translate between languages, help come up with ideas, and a lot more!")
nameresponses = ["My name is Jarvis, an intelligent and creative virtual assistant.", 
                 "I am Jarvis, a virtual assistant created by my master Nikhil.", 
                 "My name is Jarvis, inspired by Tony Stark's virtual assistant, I can help you in countless ways.", 
                 "Hi I'm Jarvis, how can I help?", 
                 "Hey, my name is Jarvis, how may I be of assistance?",
                 "My name is Jarvis, created to help those regain their creative edge, learn more, or just looking to have some fun."]
actionresponses = ["In terms of what I can do, I can tell jokes, help write a paragraph, or even help you make a decision.", 
                   "I can help you do your research, finish your sentences, or explore a topic.",
                  "Similar to Google, I can answer your questions but can also give you ideas for names or brands.",
                  "I can do many things, I am a virtual assistant.",
                  "I am here to help you, tell me- what can I do?",
                  "I can answer your strongest curiosities."]

openai.api_key = st.secrets["APIKEY"]
exitlist = ['bye', 'goodbye','see you','adios', 'cya', 'gtg', ]
fill=''
tokenmax=130
option = st.selectbox(
'Choose a specific command',('Unslected', 'Create an image', 'Write a rap', 'Write a poem','Write an article', 'Generate ideas', 'Continue writing','Translate to English','Translate to Spanish','Translate to French', 'Translate to German','Translate to Japanese','Translate to Italian','Translate to Hindi'))

question = st.text_input("Enter your prompt below:", fill)


if question:
    #language translations
    if option == 'Create an image':
        response = openai.Image.create(
        prompt=question,
        n=1,
        size="1024x1024"
)
        answer = response['data'][0]['url']
        
        with st.container():
            st.image(answer)


    if option == 'Translate to Spanish':
        question = ('Translate to Spanish: ' + question)
        tokenmax = 50
    elif option == 'Translate to English':
        question = ('Translate to English: ' + question)
        tokenmax = 50
    elif option == 'Translate to French':
        question = ('Translate to French: ' + question)
        tokenmax = 50
    elif option == 'Translate to German':
        question = ('Translate to German: ' + question)
        tokenmax = 50
    elif option == 'Translate to Japanese':
        question = ('Translate to Japanese: ' + question)
        tokenmax = 50
    elif option == 'Translate to Italian':
        question = ('Translate to Italian: ' + question)
        tokenmax = 50
    elif option == 'Translate to Hindi':
        question = ('Translate to Hindi: ' + question)
        tokenmax = 50
    #other commands
    elif option == 'Write an article':
        question = ('Write an article about: ' + question)
        
    elif option == 'Generate an idea':
        question = ('Ideas for ' + question)
        
    elif option == 'Continue writing':
        question = ('Continue writing ' + question)
        
    elif option == 'Write a rap':
        question = ('Make a rap about ' + question)
        
    elif option == 'Write a poem':
        question = ('Make a poem about ' + question)
    
    
    
    index = random.randint(0,7)
    n = st.write(notif[index])
    
    if ("your name" in question) or ("ur name" in question):
        time.sleep(0.5)
        answer = (nameresponses[(random.randint(0,5))])
    if ("you do" in question) or ("u do" in question):
        time.sleep(0.5)
        answer = (actionresponses[(random.randint(0,5))])
       
    with st.container():
        st.write(answer)

    else:
        response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0.3, max_tokens=tokenmax, top_p=1.0)
        answer = (response.choices[0].text).strip()


        with st.container():
            st.write(answer)
        
        
st.caption("Copyright Nikhil Krishnaswamy 2022")


