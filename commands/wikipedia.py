import wikipedia as wiki
from config import USER_ID


async def wiki_info(client, message):
    if message.from_user.id == USER_ID:
       await client.send_message(message.chat.id, f"{wiki.summary(message.text)}")
