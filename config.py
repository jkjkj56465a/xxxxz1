import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 29572784))

    API_HASH = os.environ.get("API_HASH", "dd81eecc41c509ebeb5bf93742667ff4")

    
