import json
import os

import pytz
from apscheduler.schedulers.asyncio import AsyncIOScheduler

import config
from BADMUSIC.core.bot import BADBOT
from BADMUSIC.core.dir import dirr
from BADMUSIC.core.git import git
from BADMUSIC.core.userbot import Userbot
from BADMUSIC.misc import dbb, heroku, sudo

from .logging import LOGGER

# time zone
TIME_ZONE = pytz.timezone(config.TIME_ZONE)
scheduler = AsyncIOScheduler(timezone=TIME_ZONE)

dirr()

git()

dbb()

heroku()

sudo()

app = BADBOT()

userbot = Userbot()

from .platforms import PlaTForms

Platform = PlaTForms()
HELPABLE = {}
