# If you are kanging this, make sure to give credits else you are gay no doubt in that..!!!


from sahuspam import *
from sahuspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from telethon import events
from telethon import version


master = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"


alive_msg = f"""
{BIO_MSG}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✪ Master:- {master}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✪ Bot Version:- `{BOT_VERSION}`
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✪ Creator:- [vijay sahu](t.me/vijaysahu_1)
➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✪ Telethon Version:- `{version.__version__}`

© @sahuspambot 
"""

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/alive'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/alive'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/alive'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/alive'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/alive'))
async def alive(e):
    if e.sender_id in MY_USERS:
        try:
            await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=alive_msg)
        except Exception as e:
            print(e)
