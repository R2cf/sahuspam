# If you are kanging this, make sure to give credits else you are gay no doubt in that..!!!


import random
from sahuspam import *
from sahuspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from sahuspam.helpers.gspam import GSPAM
from telethon import events

enemy = []

@SpamBot1.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/replyraid'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/replyraid'))
async def replyraid(e):
    if e.sender_id in MY_USERS:
        name = e.sender.first_name
        user_id = e.sender_id
        mention = f"[{name}](tg://user?id={user_id})"
        me = await SpamBot1.get_me()
        global enemy
        if e.is_reply is True:
            replied = await e.get_reply_message()
            get_name = replied.sender.first_name
            get_id = replied.sender.id
            tag = f"[{get_name}](tg://user?id={get_id})"
            try:
                if get_id in DEV_USERS:
                    await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे` {tag} `ये तेरा बाप है इसको गली देगा तेरी मां चोद देगा!`")
                elif get_id == OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                elif get_id in CO_OWNER_ID:
                    await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                elif get_id  in SUDO_USERS:
                    await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                elif get_id == me.id:
                    await e.client.send_message(e.chat_id, "`I'm Not Going To Take Action's on Myself!`")
                else:
                    message = await e.client.send_message(e.chat_id, f"`तुम्हारी मां चुदाना चालू हो रहा है .....!`")
                    if get_id in enemy:
                        await e.client.edit_message(message, f"`तुम्हारी मां पहले से चूड रही है` {tag}!")
                    else:
                        enemy.append(get_id)
                        await e.client.edit_message(message, f"`तुम्हारी मां चुदाना चालू हो गया` {tag}!")
                        print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "`गलत है!`")
        else:
            text = e.raw_text[11:]
            try:
                if text == "":
                    await e.client.send_message(e.chat_id, "`किसकी मां चोदना है tag करो!`")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    if get_id in DEV_USERS:
                        await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे` {tag} `ये तेरा बाप है इसको गली देगा तेरी मां चोद देगा!`")
                    elif get_id == OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                    elif get_id in CO_OWNER_ID:
                        await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                    elif get_id  in SUDO_USERS:
                        await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                    elif get_id == me.id:
                        await e.client.send_message(e.chat_id, f"`हेलो` {mention} `बेटे! मैं अपने owner को गली नही दूंगा तेरी मां चोदूंगा!`")
                    else:
                        message = await e.client.send_message(e.chat_id, f"`तुम्हारी मां चुदाना चालू हो रहा है.....!`")
                        if get_id in enemy:
                            await e.client.edit_message(message, f"`तुम्हारी मां पहले से चूड रही है` {tag}!")
                        else:
                            enemy.append(get_id)
                            await e.client.edit_message(message, f"`तुम्हारी मां चुदाना चालू हो गया` {tag}!")
                            print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "गलत है!")


@SpamBot1.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot2.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot3.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot4.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
@SpamBot5.on(events.NewMessage(incoming=True, pattern='/dreplyraid'))
async def dreplyraid(e):
    if e.sender_id in MY_USERS:
        global enemy
        if e.is_reply is True:
            try:
                replied = await e.get_reply_message()
                get_name = replied.sender.first_name
                get_id = replied.sender.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                message = await e.client.send_message(e.chat_id, f"`तुम्हारी मां चुदाना बंद हो रहा है.....!`")
                if get_id not in enemy:
                    await e.client.edit_message(message, f"`अभी किसी की मां नही चूड़ रही है` {tag}!")
                else:
                    enemy.remove(get_id)
                    await e.client.edit_message(message, f"`तुम्हारी मां चुदाना बंद हो गया` {tag}!")
                    print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "गलत है!")
        else:
            try:
                text = e.raw_text[11:]
                if text == "":
                    await e.client.send_message(e.chat_id, "`tag करो किसकी मां को चोद ना रोकना है!`")
                else:
                    entity = await e.client.get_entity(text)
                    get_name = entity.first_name
                    get_id = entity.id
                    tag = f"[{get_name}](tg://user?id={get_id})"
                    message = await e.client.send_message(e.chat_id, f"`तुम्हारी मां चुदाना बंद हो रहा है.....!`")
                    if get_id not in enemy:
                        await e.client.edit_message(message, f"`अभी किसी की मां नही चूड़ रही है` {tag}!")
                    else:
                        enemy.remove(get_id)
                        await e.client.edit_message(message, f"`अब तेरी मां चुदान बंद हो गया` {tag}!")
                        print(enemy)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "`गलत है!`")

@SpamBot1.on(events.NewMessage(incoming=True))
@SpamBot2.on(events.NewMessage(incoming=True))
@SpamBot3.on(events.NewMessage(incoming=True))
@SpamBot4.on(events.NewMessage(incoming=True))
@SpamBot5.on(events.NewMessage(incoming=True))
async def fuck(e):
    global enemy
    message1 = random.choice(GSPAM)
    message2 = random.choice(GSPAM)
    message3 = random.choice(GSPAM)
    message4 = random.choice(GSPAM)
    victim = e.message.id
    if e.sender_id in enemy:
        await e.client.send_message(e.chat_id, message1, reply_to=victim)
        await e.client.send_message(e.chat_id, message2, reply_to=victim)
        await e.client.send_message(e.chat_id, message3, reply_to=victim)
        await e.client.send_message(e.chat_id, message4, reply_to=victim)
