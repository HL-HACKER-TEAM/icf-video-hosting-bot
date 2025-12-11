# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = 25976192
    API_HASH = "8ba23141980539b4896e5adbc4ffd2e2"
    BOT_TOKEN = "8255788054:AAE0wJ5NDY5b_T_tai8y5Awyb77Rw8KXFas"
    name = "filetolinkvjbot"
    SLEEP_THRESHOLD = 60
    WORKERS = 4
    BIN_CHANNEL = -1003350129581
    PORT = 8080
    BIND_ADRESS = 0.0.0.0
    PING_INTERVAL = 1200
    OWNER_ID = 6621572366  
    NO_PORT = "False"
    APP_NAME = None
    OWNER_USERNAME = "RS_WONER"
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = "RS_ANIME"
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',False))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = "mongodb+srv://RAHAT1132:RAHAT11a@rahat.txn4lkk.mongodb.net/?appName=Rahat"
    UPDATES_CHANNEL = "CARTOONFUNNY03"
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
