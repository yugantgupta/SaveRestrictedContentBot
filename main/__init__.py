#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", "22233521", cast=int)
API_HASH = config("API_HASH", "dfad40fe3665377983903737cc05cfbc")
BOT_TOKEN = config("BOT_TOKEN", "8736368440:AAGqGxVFBSE1RX2TXTIHYhKMdYc6si0iOGY")
SESSION = config("SESSION", "AgFitqsAenE5VA-iuME_ym36NSBXf6gbqIkTj0sqLg_iFj92pwAw9Pj7aEaXVddxKgS5uFCtDdPwv9LL4jg7so3jVIdowbaOkNdWZdlN3Ty0-VW6k6c92itR1666b07VtPecDWbYO2_IVJmymAplmo6PbKlouIKXTt9kGFmP8-HiYk4W3RcPUcqPlba5cor4dOLj1_crQbrq8UQKOEuEBJz92eS-B05O-jy_6ZplzHr3_LFPtXK1nuL_Cu_cyX0loOjaZpcMB9uRBTwX-9mcCVLk4RNWQjz20mD7Fozgjjfk3qVVYao5GO6qWXwDmSkr9OpHmQOZHCkWmgPo5cjtA4E4LFBgdgAAAAE7y3eaAA", default=None)
FORCESUB = config("FORCESUB", "saverest091")
AUTH = config("AUTH", "5298157466", cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
