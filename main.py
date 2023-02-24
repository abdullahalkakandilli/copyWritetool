import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os

def _max_width_():
    max_width_str = f"max-width: 1800px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
st.set_page_config(page_icon="✂️", page_title="Question to Image")


openai_key = st.sidebar.text_area("Enter your OpenAI key")
st.write(openai_key)

c2, c3 = st.columns([6, 1])

with c2:
    c31, c32 = st.columns([12, 2])
    with c31:
        st.caption("")
        st.title("Question")
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


c29, c30, c31 = st.columns([1, 1, 2])

with c29:

  st.write(answer_)