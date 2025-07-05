# Whisper dependencies
# !pip install -q git+https://github.com/openai/whisper.git
# !sudo apt-get install ffmpeg

# !pip install -q deep-translator


# OpenAI GPT API (optional for NLP extraction)
# !pip install -q openai

import whisper
from deep_translator import GoogleTranslator
import openai
import json

# Load Whisper model
model = whisper.load_model("small")  # or "medium"/"large" if GPU available

# 🎙 Step 1: Transcribe native language audio
def transcribe_audio(audio_file_path):
    result = model.transcribe(audio_file_path)
    return result['text']

# 🌐 Step 2: Translate to English
def translate_text(text, target_lang="en"):
    return GoogleTranslator(source='auto', target=target_lang).translate(text)

# 🤖 Step 3: Extract structured listing info
def extract_listing_info(prompt_text):
    openai.api_key = "OpenAi API Key"  # 🔑 Replace with your key

    system_prompt = """
You are a voice listing assistant for rural commerce. 
From the following English sentence, extract this information:
- product name
- quantity
- price per unit (in rupees)

Return JSON like:
{"product": "", "quantity": , "price_per_unit": }
"""
    from openai import OpenAI

    client = OpenAI(api_key="OpenAi API Key")  # your API key here

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt_text}
        ]
    )

    return response.choices[0].message.content


# 🚀 Full Pipeline
def full_pipeline(audio_path):
    print("🔊 Transcribing...")
    native_text = transcribe_audio(audio_path)
    print(f"📝 Native Transcription: {native_text}")

    print("🌐 Translating...")
    english_text = translate_text(native_text)
    print(f"🌍 Translated to English: {english_text}")

    print("🤖 Extracting structured info...")
    listing_json = extract_listing_info(english_text)
    print(f"📦 Structured Listing JSON: {listing_json}")

    return listing_json
# Replace with your uploaded file name
full_pipeline("vendor_input_tamil.mp3")
