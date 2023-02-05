from pyrogram import Client
from pyrogram.handlers import MessageHandler

from commands.TTS import send_tts_message
from config import API_ID, API_HASH

app = Client(
    "user_bot",
    API_ID,
    API_HASH,
    hide_password=True
)

app.add_handler(MessageHandler(send_tts_message))

app.run()
