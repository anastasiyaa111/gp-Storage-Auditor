import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GP_HOST = os.getenv("GP_HOST", "localhost")
    GP_PORT = os.getenv("GP_PORT", "5432")
    GP_DB = os.getenv("GP_DB", "postgres")
    GP_USER = os.getenv("GP_USER", "gpadmin")
    GP_PASSWORD = os.getenv("GP_PASSWORD", "")
    
    TARGET_TABLES = os.getenv("TARGET_TABLES", "").split(",")

    @property
    def db_params(self):
        return {
            "host": self.GP_HOST,
            "port": self.GP_PORT,
            "database": self.GP_DB,
            "user": self.GP_USER,
            "password": self.GP_PASSWORD
        }

settings = Settings()
