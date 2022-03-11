import os
from dotenv import load_dotenv
import secrets

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))



class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or secrets.token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or\
        f'sqlite:///{os.path.join(basedir, "db.sqlite")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    APIFAIRY_TITLE = 'Zoo-App API'
    APIFAIRY_VERSION = '1.0'
    APIFAIRY_UI = os.environ.get('DOCS_UI', 'elements')