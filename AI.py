##imports
import streamlit as st 
#streamlit is the module I used to take my existing code and make it into a website
import os
import openai #main module which actually answers the query and sends the result back
import random #for random num/index generator
import time #for adding delays

##configuration
st.set_page_config(page_title="Jarvis AI", page_icon=":tada:")

#adding background image for website
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
background-image: url("https://images.unsplash.com/photo-1525548002014-e18135d814d7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2940&q=80");
opacity: 1;
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
                 "I am Jarvis, a virtual assistant created by my master", 
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
#connecting API to openai davinci engine (hidden for security reasons)
openai.api_key = st.secrets["APIKEY"]
tokenmax=130
option = st.selectbox(
'Choose a specific command',('Unslected', 'Write a poem','Write an article', 'Generate ideas', 'Continue writing','Translate to English','Translate to Spanish','Translate to French', 'Translate to German','Translate to Japanese','Translate to Italian','Translate to Hindi'))
fill = ''
question = st.text_input("Enter your prompt below:", fill)

#this function takes the query and send it to openai to get a response
def main(question):
    #sending to OPENAI to find an answer
	response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0.3, max_tokens=tokenmax, top_p=1.0)
		#indexing the result from Open AI
	answer = (response.choices[0].text).strip()
        #printing answer 
	with st.container():
		st.write(answer)
#if there is something in the input box, it will send it to openai by running main()
if question:
    #adding language translation request to query
    if option == 'Translate to Spanish':
        question = ('Translate to Spanish: ' + question)
        tokenmax = 50
    elif option == 'Translate to English':
        question = ('Translate to English: ' + question)
        tokenmax = 50
    elif option == 'Translate to French':
        question = ('Translate to French: ' + question)
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
    elif option == 'Write a poem':
        question = ('Make a poem about ' + question) 
    #let the user know it is loading    
    index = random.randint(0,7)
    st.write(notif[index])
    # hard coding a few responses to make it more personalized
    if ("you do" in question) or ("u do" in question):
        time.sleep(0.5)
        st.write(actionresponses[(random.randint(0,5))])
        
    if ("your name" in question) or ("ur name" in question):
        time.sleep(0.5)
        st.write(nameresponses[(random.randint(0,5))])
    else:
      st.write("go away vishresh) # this calls the main() function defined above
      
