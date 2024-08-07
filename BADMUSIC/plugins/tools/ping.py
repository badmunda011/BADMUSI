from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
import config
from strings import get_command
from BADMUSIC import app
from BADMUSIC.core.call import BAD
from BADMUSIC.utils import bot_sys_stats
from BADMUSIC.utils.decorators.language import language

@app.on_message(filters.command(["ping"]))
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await BADMUSIC.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_3"])
    await response.edit_text(
        _["ping_4"])
    await response.edit_text(
        _["ping_2"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
       _["ping_5"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_6"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_7"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_8"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_9"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_10"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_11"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ))
    await response.edit_text(
        _["ping_12"].format(
            resp, MUSIC_BOT_NAME, UP, RAM, CPU, DISK, pytgping
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [
            InlineKeyboardButton(
                text="✚  𝐀𝐃𝐃 𝐌𝐄 𝐈𝐍 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏  ✚",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        
        ],
        [
            InlineKeyboardButton(
                text="♦️𝐆𝐑𝐎𝐔𝐏♦️", url=f"https://t.me/THE_DRAMA_CLUB_01",
            ),
            InlineKeyboardButton(
                text="♦️𝐌𝐎𝐑𝐄♦️", url=f"https://t.me/BAD_MUNDA_0",
            )
        ],
        [
            InlineKeyboardButton(
                text="⚙️ 𝐇𝐄𝐋𝐏 ⚙️", callback_data="settings_back_helper"
            )
        ],
    ]
    ),
)
    
        
