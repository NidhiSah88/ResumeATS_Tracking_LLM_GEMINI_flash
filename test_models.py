import os
from dotenv import load_dotenv

load_dotenv()

import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

for model in genai.list_models():
    print(model.name)


# test_models.py
import google.generativeai as genai
print("Gemini import OK")