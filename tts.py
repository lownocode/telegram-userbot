from gtts import gTTS
from config.cfg import language, tts_speed


def text_to_speech(user_message):
    text_val = user_message
    lang = language
    speed = tts_speed

    obj = gTTS(text=text_val, lang=lang, slow=speed)
    obj.save("voices/speech.ogg")
