from gtts import gTTS
from config import language, tts_speed
import os

def text_to_speech(user_message):
    text_val = user_message
    lang = language
    speed = tts_speed

    obj = gTTS(text=text_val, lang=lang, slow=speed)
    try:
        return obj.save("voices/speech.ogg")
    except FileNotFoundError:
        os.system("mkdir voices")
        return obj.save("voices/speech.ogg")
