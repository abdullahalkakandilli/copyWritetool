import os
import openai
import dotenv
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
#os.getenv

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Write me a blog post about data cleaning:",
  temperature=0.3,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

print(response.choices[0].text)