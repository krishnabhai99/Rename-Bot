# (c) @AbirHasan2005

import os
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)


class Config(object):
    API_ID = int(os.environ.get("26387127", ""))
    API_HASH = os.environ.get("19718ab7acd97d0f71ada2807ddfe47a", "")
    BOT_TOKEN = os.environ.get("7869228468:AAHeZrz3IjY5wwYrsmwahqvpNG1PyNwox-0", "")
    DOWNLOAD_DIR = os.environ.get("DOWNLOAD_DIR", "./downloads")
    LOGGER = logging
    OWNER_ID = int(os.environ.get("5446367898", 1445283714))
    PRO_USERS = list(set(int(x) for x in os.environ.get("5446367898", "0").split()))
    PRO_USERS.append(OWNER_ID)
    MONGODB_URI = os.environ.get("mongodb+srv://Shivam9910:@Shivam99108870@cluster0.na2ub.mongodb.net/", "")
    LOG_CHANNEL = int(os.environ.get("-1002375585159", "-100"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
