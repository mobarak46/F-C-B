import os
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv("TOKEN")
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(","))) if os.getenv("ADMIN_IDS") else []

import re

from os import environ

from Script import script 



id_pattern = re.compile(r'^.\d+$')



# Bot information

SESSION = environ.get('SESSION', 'Media_search')

API_ID = int(environ.get('API_ID', ''))

API_HASH = environ.get('API_HASH', '')

BOT_TOKEN = environ.get('BOT_TOKEN', "")



# This Pictures Is For Start Message Picture, You Can Add Multiple By Giving One Space Between Each.

PICS = (environ.get('PICS', 'https://i.ibb.co/Q3qqkF71/x.jpg https://i.ibb.co/TJ5JdQR/x.jpg https://i.ibb.co/d433j46Z/x.jpg https://i.ibb.co/60jTMLMj/x.jpg https://i.ibb.co/TBWjyQdV/x.jpg https://i.ibb.co/Z6nDcZyg/x.jpg https://i.ibb.co/23QWvRfc/x.jpg https://i.ibb.co/DPjsyCgt/x.jpg https://i.ibb.co/3yJGPK8z/x.jpg https://i.ibb.co/F4NBM99C/x.jpg https://i.ibb.co/Z1T97h5q/x.jpg https://i.ibb.co/Z1FTxX0r/x.jpg https://i.ibb.co/G4w5QjVN/x.jpg https://i.ibb.co/zTdJw86t/x.jpg https://i.ibb.co/wFmLvYG0/x.jpg https://i.ibb.co/WN3j2P3p/x.jpg https://i.ibb.co/p6zj7Kw8/x.jpg https://i.ibb.co/3yjGPSDP/x.jpg https://i.ibb.co/27CXGp2b/x.jpg https://i.ibb.co/Xrq7JHfd/x.jpg https://i.ibb.co/mCTW950v/x.jpg')).split()



# Admins & Users

ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1491400016 8079968449').split()] # For Multiple Id Use One Space Between Each.

auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1491400016 8079968449').split()]  # For Multiple Id Use One Space Between Each.

AUTH_USERS = (auth_users + ADMINS) if auth_users else []

LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002058704187')) # This Channel Is For When User Start Your Bot Then Bot Send That User Name And Id In This Log Channel, Same For Group Also.


# MongoDB information

DATABASE_URI = environ.get('DATABASE_URI', "")# IF Multiple Database Is False Then Fill Only This Database Url.

DATABASE_NAME = environ.get('DATABASE_NAME', "") 

COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_Files')

#Modes Calls and True & False

# Premium And Referal Settings

PREMIUM_AND_REFERAL_MODE = bool(environ.get('PREMIUM_AND_REFERAL_MODE', True)) # Set Ture Or False

# Rename Info : If True Then Bot Rename File Else Not

RENAME_MODE = bool(environ.get('RENAME_MODE', False)) # Set True or False

AUTO_MODE = bool(environ.get('AUTO_MODE', False)) # Set True or False



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

MUBI_FILE_CAPTION = environ.get("MUBI_FILE_CAPTION", f"{script.CAPTION}"




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





















































