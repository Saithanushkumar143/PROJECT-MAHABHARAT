import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def get_ai_based_wisdom(query):
    prompt = f"""
You are a wise mentor inspired by the Mahabharata. 
Respond to this user's problem with motivational advice using examples from Arjuna, Krishna, Karna, and others characters in mahabharata in simple English.

Query: "{query}"



Format the answer like this clearly:

Response: [Short poetic and traditional wisdom paragraph
Example format:
"Arjuna too once hesitated before battle. With Krishna’s wisdom, he rose again.
Like him, your path may seem foggy now, but your inner strength can light the way."]  
Lesson: [A life lesson in one line]  
Shloka: [A Sanskrit shloka related to the advice]
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    # Extract using labels
    response_text = ""
    lesson_text = ""
    shloka_text = ""

    for line in text.splitlines():
        if line.lower().startswith("response:"):
            response_text = line.partition(":")[2].strip()
        elif line.lower().startswith("lesson:"):
            lesson_text = line.partition(":")[2].strip()
        elif line.lower().startswith("shloka:"):
            shloka_text = line.partition(":")[2].strip()

    return {
        "response": response_text or "No response",
        "lesson": lesson_text or "No lesson",
        "shloka": shloka_text or "No shloka"
    }
