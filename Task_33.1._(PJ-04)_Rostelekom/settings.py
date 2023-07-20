import os
from dotenv import load_dotenv

load_dotenv()

valid_email = os.getenv('valid_email')
valid_phone = os.getenv('valid_phone')
valid_password = os.getenv('valid_password')

URL = 'https://b2c.passport.rt.ru'

PATH = './chromedriver.exe'







