from sahuspam import *
from sahuspam import SpamBot1, SpamBot2, SpamBot3, SpamBot4, SpamBot5
from sahuspam.help import *
from sahuspam.helpers.commands import *
from telethon import events


@SpamBot1.on(events.CallbackQuery(data=b'alive'))
@SpamBot2.on(events.CallbackQuery(data=b'alive'))
@SpamBot3.on(events.CallbackQuery(data=b'alive'))
@SpamBot4.on(events.CallbackQuery(data=b'alive'))
@SpamBot5.on(events.CallbackQuery(data=b'alive'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{ALIVE_CMD}", buttons=BACK)



@SpamBot1.on(events.CallbackQuery(data=b'ping'))
@SpamBot2.on(events.CallbackQuery(data=b'ping'))
@SpamBot3.on(events.CallbackQuery(data=b'ping'))
@SpamBot4.on(events.CallbackQuery(data=b'ping'))
@SpamBot5.on(events.CallbackQuery(data=b'ping'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PING_CMD}", buttons=BACK)





@SpamBot1.on(events.CallbackQuery(data=b'raid'))
@SpamBot2.on(events.CallbackQuery(data=b'raid'))
@SpamBot3.on(events.CallbackQuery(data=b'raid'))
@SpamBot4.on(events.CallbackQuery(data=b'raid'))
@SpamBot5.on(events.CallbackQuery(data=b'raid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{RAID_CMD}", buttons=BACK)



@SpamBot1.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot2.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot3.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot4.on(events.CallbackQuery(data=b'replyraid'))
@SpamBot5.on(events.CallbackQuery(data=b'replyraid'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{REPLYRAID_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'spam'))
@SpamBot2.on(events.CallbackQuery(data=b'spam'))
@SpamBot3.on(events.CallbackQuery(data=b'spam'))
@SpamBot4.on(events.CallbackQuery(data=b'spam'))
@SpamBot5.on(events.CallbackQuery(data=b'spam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{SPAM_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'back'))
@SpamBot2.on(events.CallbackQuery(data=b'back'))
@SpamBot3.on(events.CallbackQuery(data=b'back'))
@SpamBot4.on(events.CallbackQuery(data=b'back'))
@SpamBot5.on(events.CallbackQuery(data=b'back'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit("Here is the Help Menu for using Your Sahu Spam Bot..!!!", buttons=Buttons)

@SpamBot1.on(events.CallbackQuery(data=b'pspam'))
@SpamBot2.on(events.CallbackQuery(data=b'pspam'))
@SpamBot3.on(events.CallbackQuery(data=b'pspam'))
@SpamBot4.on(events.CallbackQuery(data=b'pspam'))
@SpamBot5.on(events.CallbackQuery(data=b'pspam'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{PSPAM_CMD}", buttons=BACK)


@SpamBot1.on(events.CallbackQuery(data=b'extras'))
@SpamBot2.on(events.CallbackQuery(data=b'extras'))
@SpamBot3.on(events.CallbackQuery(data=b'extras'))
@SpamBot4.on(events.CallbackQuery(data=b'extras'))
@SpamBot5.on(events.CallbackQuery(data=b'extras'))
async def no(e):
    if e.query.user_id not in MY_USERS:
        await e.answer("You can't access these buttons. Make Your Own @vijaysahu_1..!!!", cache_time=0, alert=True)
    else:
        await e.edit(f"{EXTRA_CMD}", buttons=BACK)
