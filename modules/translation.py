from googletrans import Translator
from langdetect import detect

# Initialize the Google Translator object
translator = Translator()

# Try to detect language or return to default (English) in case of detection failure
def detect_language(text: str) -> str:
    try:
        return detect(text)
    except:
        return 'en'                     

# Translates any given text into English
def translate_to_english(text: str, src_lang: str) -> str:
    if src_lang == 'en':
        return text
    result = translator.translate(text, src='auto', dest='en')
    return result.text

# Translates English text into another language
def translate_from_english(text: str, dest_lang: str) -> str:
    if dest_lang == 'en':
        return text
    result = translator.translate(text, src='en', dest=dest_lang)
    return result.text
