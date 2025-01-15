from random import choice

from pyrogram import Client, filters
from pyrogram.types import Message

from BADMUSIC.cplugin.utils.data import GROUP, PBIRAID, VERIFIED_USERS

# import
from BADMUSIC.misc import SUDOERS as SUDO_USER

# pbiraid


@Client.on_message(filters.command("pbiraid", prefixes=".") & SUDO_USER)
async def raid(Client: Client, m: Message):
    Bad = "".join(m.text.split(maxsplit=1)[1:]).split(" ", 2)
    if len(Bad) == 2:
        counts = int(Bad[0])
        username = Bad[1]
        if not counts:
            await m.reply_text(f"PBIRAID LIMIT NOT FOUND PLEASE GIVE COUNT!")
            return
        if not username:
            await m.reply_text(
                "you need to specify an user! Reply to any user or gime id/username"
            )
            return
        try:
            user = await Client.get_users(Bad[1])
        except:
            await m.reply_text("**Error:** User not found or may be deleted!")
            return
    elif m.reply_to_message:
        counts = int(Bad[0])
        try:
            user = await Client.get_users(m.reply_to_message.from_user.id)
        except:
            user = m.reply_to_message.from_user
    else:
        await m.reply_text("Usage: .pbiraid count username or reply")
        return
    if int(m.chat.id) in GROUP:
        await m.reply_text("**Sorry !! i Can't Spam Here.**")
        return
    if int(user.id) in VERIFIED_USERS:
        await m.reply_text("I can't Pbiraid on my developer")
        return
    if int(user.id) in SUDO_USER:
        await m.reply_text("This guy is a sudo users.")
        return
    mention = user.mention
    for _ in range(counts):
        r = f"{mention} {choice(PBIRAID)}"
        await Client.send_message(m.chat.id, r)
        await asyncio.sleep(0.3)
