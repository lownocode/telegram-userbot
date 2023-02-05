from utils.tts import text_to_speech

from config import USER_ID


async def send_tts_message(client, message):
    if message.from_user.id == USER_ID:
        text_to_speech(message.text)

    await client.delete_messages("me", message_ids=message.id, revoke=True)
    await client.send_voice(message.chat.id, "voices/speech.ogg")
