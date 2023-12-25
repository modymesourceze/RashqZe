import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 25721707))

    API_HASH = os.environ.get("API_HASH", "c6a2826bd6bce80a2ea20a444fe2a934")
