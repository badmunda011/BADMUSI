from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from BADMUSIC.core.call import BAD as BAD
from BADMUSIC.utils.database import is_music_playing, music_off
from BADMUSIC.utils.decorators import AdminRightsCheck
from config import BANNED_USERS


@Client.on_message(
    filters.command(["pause", "cpause"], prefixes=["."]) & filters.group & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await BAD.pause_stream(chat_id)

    buttons = [
        [
            InlineKeyboardButton(
                text="ʀᴇsᴜᴍᴇ", callback_data=f"ADMIN Resume|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ʀᴇᴘʟᴀʏ", callback_data=f"ADMIN Replay|{chat_id}"
            ),
        ],
    ]

    await message.reply_text(
        _["admin_2"].format(message.from_user.mention),
        reply_markup=InlineKeyboardMarkup(buttons),
    )


__MODULE__ = "Pause"
__HELP__ = """
**Pause Music**

This module allows administrators to pause the music playback in the group.

Commands:
- /pause: Pause the music playback in groups.
- /cpause: Pause the music playback in channels.

Note:
- Only administrators can use these commands.
"""
