import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the API
genai.configure(api_key='AIzaSyCOK4DZmBMg4iIFcIIC9JqKqrmeqZUvZlM')

# Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

def ask_llm(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"LLM Error: {e}"
