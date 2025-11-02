import re
from os import environ

# Bot Session Name
SESSION = environ.get('SESSION', 'TechVJBot')

# Your Telegram Account Api Id And Api Hash
API_ID = int(environ.get('API_ID', '27829715'))
API_HASH = environ.get('API_HASH', '72e38250de2b0ae7dd9eb467ffa35c17')

# Bot Token, This Is Main Bot
BOT_TOKEN = environ.get('BOT_TOKEN', "8595685929:AAHkfvg0-7LHrdeLL_hORYFyzmFUPBbBnqU")

# Admin Telegram Account Id For Withdraw Notification Or Anything Else
ADMIN = int(environ.get('ADMIN', '2034253345'))

# Back Up Bot Token For Fetching Message When Floodwait Comes
BACKUP_BOT_TOKEN = environ.get('BACKUP_BOT_TOKEN', "8503618705:AAGfTZzGYEyeyJ1Alim4xX7E6ZzPms4tx4w")

# Log Channel, In This Channel Your All File Stored.
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002682603345'))

# Mongodb Database For User Link Click Count Etc Data Store.
MONGODB_URI = environ.get("MONGODB_URI", "mongodb+srv://rdx27652:<mQTZczyeyYOEM9qo>@cluster0.d7v1xoh.mongodb.net/?appName=Cluster0")

# Stream Url Means Your Deploy Server App Url, Here You Media Will Be Stream And Ads Will Be Shown.
STREAM_URL = environ.get("STREAM_URL", "https://yoursmilesteam.blogspot.com/2025/11/stream.html")

# This Link Used As Permanent Link That If Your Deploy App Deleted Then You Change Stream Url, So This Link Will Redirect To Stream Url.
LINK_URL = environ.get("LINK_URL", "")

# Others, Not Usefull
PORT = environ.get("PORT", "8080")
MULTI_CLIENT = False
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
