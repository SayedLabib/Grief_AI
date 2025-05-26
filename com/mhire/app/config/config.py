import os
from dotenv import load_dotenv
            
load_dotenv()

class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Config, cls).__new__(cls)
            cls._instance.gemini_api_key = os.getenv("GEMINI_API_KEY")
            cls._instance.gemini_api_model = "gemini-2.0-flash"
            cls._instance.tavily_api_key = os.getenv("TAVILY_API_KEY")

        return cls._instance