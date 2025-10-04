import os

from dotenv import load_dotenv


load_dotenv()

OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY')
OPENROUTER_BASE_URL = os.getenv('OPENROUTER_BASE_URL')
OPENROUTER_MODEL = os.getenv('OPENROUTER_MODEL')
