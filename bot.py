import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get("25742241"))
API_HASH = environ.get("6d158174dd23c6cafbd99aff6ae1ba48")
BOT_TOKEN = environ.get("6010383835:AAHgVrnF4tkEvl8cbQHdaWEJjlBNZmk1jjY")
SESSION = environ.get("SESSION")
TIME = int(environ.get("300"))
GROUPS = []
for grp in environ.get("-1001738037090").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get("5981826686 800422840").split():
    ADMINS.append(int(usr))

START_MSG = "<b>Hai {},\nI'm a private bot of @mh_world to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
       
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
