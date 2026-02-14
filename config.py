from json import load
import os
from dotenv import load_dotenv

load_dotenv()

AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "5962156884:AAEBOd5crk8SWWQFZueWVOs2m_-Bx_UXBRM")
