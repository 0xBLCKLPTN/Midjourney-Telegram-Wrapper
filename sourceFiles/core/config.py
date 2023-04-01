from pydantic import BaseSettings
from python_dotenv import load_dotenv

try:
    load_dotenv()
except Exception as ex:
    pass

class Settings(BaseSettings):
    accounts_fp: str
    channel_url: str

settings = Settings()

