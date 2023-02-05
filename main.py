from pyrogram import Client
from pyrogram.handlers import MessageHandler

from commands.TTS import send_tts_message
from config.cfg import API_ID, API_HASH

app = Client("tts_bot", API_ID, API_HASH)

app.add_handler(MessageHandler(send_tts_message))

app.run()
