import openai
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from jose import jwt
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


st.set_page_config(page_icon="images/icon.png", page_title="Copywriter Tool")


openai.api_key = os.getenv('OPEN_API_KEY')
try:

    token = st.experimental_get_query_params()['token'][0]

except:

    raise Exception('NaN Token!')

try:
    payload = jwt.decode(token, key=os.getenv('JWT_SECRET'), options={"verify_signature": True,
                                                                        "verify_aud": False,
                                                                        "verify_iss": False})

except:
    raise Exception('Invalid Token!')


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
