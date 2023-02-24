import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

max_width_str = f"max-width: 1800px;"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style,  unsafe_allow_html=True,
)


#st.set_page_config(page_icon="images/icon.png", page_title="Copywriter Tool")


openai.api_key = st.sidebar.text_input(
    "Enter your OpenAI API key",
    help="Once you created you OpenAI account, you can get your free API token in your settings page: https://platform.openai.com/account/api-keys",
    type="password",
)


c2, c3 = st.columns([6, 1])

with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Copywriter Tool")
    with c32:
        st.image(
            "images/logo.png",
            width=200,
        )

# Convert PDF to JPG

def copyWriter(question_):

  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=question_,
    temperature=0.3,
    max_tokens=250,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  result = response.choices[0].text

  return (result)

form = st.form(key="annotation")

with form:
    question_ = st.text_input("Enter your query!")
    submitted = st.form_submit_button(label="Submit")

answer_ = pd.DataFrame()
if submitted:

    answer_ = copyWriter(question_)
    st.write("Your answer appear here!")
    st.write(answer_)
