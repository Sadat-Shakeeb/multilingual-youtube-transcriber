import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def chunk_text(text, chunk_size=9000):
    """
    Splits text into smaller chunks to avoid token limits.
    """
    return [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]


def convert_to_roman_urdu(text, source_language):
    """
    Converts Urdu or English text into Roman Urdu.
    """

    model = genai.GenerativeModel("models/gemini-2.5-flash")

    chunks = chunk_text(text, chunk_size=9000)
    roman_chunks = []

    for chunk in chunks:

        if source_language == "ur":
            prompt = f"""
            Convert the following Urdu text into Roman Urdu.

            Do NOT translate to English.
            Preserve meaning.
            Use natural Pakistani Roman Urdu.

            Text:
            {chunk}
            """

        elif source_language == "en":
            prompt = f"""
            Convert the following English text into Roman Urdu.
            Do NOT output Urdu script.
            Output only Roman Urdu.

            Text:
            {chunk}
            """

        else:
            raise ValueError("Only Urdu and English are supported.")

        response = model.generate_content(prompt)
        roman_chunks.append(response.text.strip())

    return "\n".join(roman_chunks)