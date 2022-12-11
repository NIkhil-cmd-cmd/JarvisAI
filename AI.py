import streamlit as st
import os
import openai
import random


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
    st.write("You can ask Jarvis to answer questions, create a paragraph, finish a sentence, help come up with ideas, and a lot more!")


# Load your API key from an environment variable or secret management service
openai.api_key = "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"
exitlist = ['bye', 'goodbye','see you','adios', 'cya', 'gtg', ]
fill=''


question = st.text_input("Enter your prompt below:", fill)

if question:
    index = random.randint(0,7)
    n = st.write(notif[index])
    
    response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0.3, max_tokens=120, top_p=1.0)
    answer = (response.choices[0].text).strip()


    with st.container():
        st.write(answer)
        
        
st.caption("Copyright Nikhil Krishnaswamy 2022")


