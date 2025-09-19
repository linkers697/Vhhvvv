import os
from dotenv import load_dotenv

load_dotenv()

# Telegram API
API_ID = int(os.getenv("API_ID", 21696829))  
API_HASH = os.getenv("API_HASH", "c0e23cf3dfa118239951a88bd0f4c6b7")

# Bot Token / String Session
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
STRING1 = os.getenv("STRING_SESSION", None)

# Database
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://music1ygffygfgdf_db_user:music1ygffygfgdf_db_user@cluster0.0lbiwen.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# Owner / Admin
OWNER_ID = int(os.getenv("OWNER_ID", 7569863273))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "YourAyush")

# Support / Updates
SUPPORT_GRP = os.getenv("SUPPORT_GRP", "HeavenChatGroup")
UPDATE_CHNL = os.getenv("UPDATE_CHNL", "AuraVisual")
