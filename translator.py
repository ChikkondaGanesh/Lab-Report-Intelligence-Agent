import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def translate_text(text, language):

    language_map = {
        "en": "English",
        "hi": "Hindi",
        "te": "Telugu",
        "ta": "Tamil"
    }

    target_language = language_map.get(language, "English")

    prompt = f"""
    Translate the following medical report into {target_language}.
    Only return the translated text.
    Do not mix languages.

    Text:
    {text}
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional medical translator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
    #..