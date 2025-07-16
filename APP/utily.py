import os
# import google.generativeai as genai
import requests
from sqlalchemy.orm import Session
from crud import update_translation_task
OLLAMA_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "deepseek-r1:1.5b"

def perform_translation(task_id: int, text: str, languages: list, db: Session):
    translations = {}

    for lang in languages:
        try:
            prompt = f"Translate the following text to {lang}:\n\n{text}"
            payload = {
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            }
            response = requests.post(OLLAMA_URL,json=payload)
            data=response.json()
            translated_text = data.get("response","").strip()
            translations[lang] = translated_text

        except Exception as e:
            print(f"Error translating to {lang}: {e}")
            translations[lang] = f"Error: {e}"

    update_translation_task(db, task_id, translations)
