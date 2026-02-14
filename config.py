from json import load
import os
from dotenv import load_dotenv

load_dotenv()

AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://melrnoor:<db_wanaalkq>@cluster0.46zkpgr.mongodb.net/?appName=Cluster0")
BOT_TOKEN = os.environ.get('bot_token', "5962156884:AAEBOd5crk8SWWQFZueWVOs2m_-Bx_UXBRM")
