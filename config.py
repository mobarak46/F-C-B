import os
import re
from os import environ
from Script import script 
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
API_ID = int(os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
OWNER_IDS = list(map(int, os.getenv("OWNER_IDS", "").split(","))) if os.getenv("OWNER_IDS") else []



id_pattern = re.compile(r'^.\d+$')


# Bot information

SESSION = os.getenv('SESSION', 'Media_search')

API_ID = int(environ.get('API_ID', ''))

API_HASH = environ.get('API_HASH', '')



# This Pictures Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.

PICS = (environ.get('PICS', '')).split()



# Admins & Users

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1491400016 8079968449').split()] # For Multiple Id Use One Space Between Each.

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1491400016 8079968449').split()]  # For Multiple Id Use One Space Between Each.

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '')) # This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.


# MongoDB information

DATABASE_URI = environ.get('DATABASE_URI', "")

DATABASE_NAME = environ.get('DATABASE_NAME', "")  #don't use cluser0

COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_Files')


# Rename Info : If True Then Bot Rename File Else Not

RENAME_MODE = bool(environ.get('RENAME_MODE', True)) # Set True or False

AUTO_MODE = bool(environ.get('AUTO_MODE', True)) # Set True or False



# Links

GRP_LNK = environ.get('GRP_LNK', '')

CHNL_LNK = environ.get('CHNL_LNK', '')

OWNER_LNK = environ.get('OWNER_LNK', '') # OWNER LNK Link Without https://t.me or @



# True Or False

AI_FILE_FRMT_CHECK = bool(environ.get('AI_FILE_FRMT_CHECK', True))

BOT_PM = bool(environ.get('BOT_PM', True))

UPLOAD_TO_LOG = bool(environ.get('UPLOAD_TO_LOG', True))

MAX_FILE_CNVT = bool(environ.get('MAX_FILE_CNVT', True))

AUTO_DELETE = bool(environ.get('AUTO_DELETE', True))

USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))



# Others

FILE_DELETE_TIME = int(environ.get("FILE_DELETE_TIME", "300")) #if the user set auto delete

MAX_FILE_CNVT = environ.get("MAX_FILE_CNVT", "5") #at one time per user

PORT = environ.get("PORT", "8000")

MSG_ALRT = environ.get('MSG_ALRT', 'Wᴏʀᴋɪɴɢ 💌')

MUBI_FILE_CAPTION = environ.get("MUBI_FILE_CAPTION", f"{script.MUBI_FILE_CAPTION}") # this caption for if user didn't set custom caption this will work




MULTI_CLIENT = False

SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))

PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes

if 'DYNO' in environ:

    ON_HEROKU = True

else:

    ON_HEROKU = False

URL = environ.get("URL", "")



# Start Command Reactions

REACTIONS = ["🦋", "😇", "🤗", "😍", "👍", "🎅", "😐", "🥰", "🤩", "😱", "🤣", "😘", "👏", "😛", "😈", "🎉", "⚡️", "🫡", "🤓", "😎", "🏆", "🔥", "🤭", "🌚", "🆒", "👻", "😁"] #don't add any emoji because tg not support all emoji reactions





















































