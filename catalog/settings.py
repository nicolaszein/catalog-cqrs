import os
from dotenv import load_dotenv

load_dotenv()

COMMAND_DATABASE_URL = os.environ.get('COMMAND_DATABASE_URL', '')
