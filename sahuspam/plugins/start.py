# If you are kanging this, make sure to give credits else you are gay no doubt in that..!!!


from sahuspam import *
from sahuspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5 
from telethon import events, Button


data  = [
    Button.url("Repo", url="t.me/vijaysahu_1"),
    Button.url("Support", url="https://t.me/DANGEROUSFIGHTERGROUP")
  ]


@SpamBot1.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/start'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/start'))
async def start(e):
    if e.chat_id is e.sender_id:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        myOwner = f"[{OWNER_NAME}](tg://user?id={OWNER_ID})"
        creator = f"[VIJAY SAHU](t.me/vijaysahu_1)"
        sudo_user = ""
        if e.sender_id in MY_USERS:
            sudo_user = "True"
        else:
            sudo_user = "False"
        ON_START = f"""
हैलो {mention},
ये spam bot विजय साहू ने बनाया है अगर आपको भी बनवाना है तो @vijaysahu_1 पर massage करे 🥵🥵

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

✪ Master:- {myOwner}

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

✪ Sudo:- {sudo_user}

➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖

✪ Creator:- {creator}


© @vijaysahu_1
"""
        await e.client.send_file(e.chat_id, DISPLAY_PIC, caption=ON_START, buttons=data)
