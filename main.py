"""
main file xd
"""

import logging
from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

from commands.TTS import send_tts_message
from commands.wikipedia import wiki_info
from config import API_ID, API_HASH, USER_ID


logging.basicConfig(level=logging.INFO)


app = Client(
    "user_bot",
    API_ID,
    API_HASH,
    hide_password=True
)


@app.on_message(filters.text, group=0)
async def route(client, message):
    if message.from_user.id == USER_ID:
        match message.text.lower():
            case "voice":
                return app.add_handler(MessageHandler(send_tts_message), 1)
            case "wiki":
                return app.add_handler(MessageHandler(wiki_info), 2)

app.run()
