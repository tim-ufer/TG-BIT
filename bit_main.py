from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')

print(api_id)

