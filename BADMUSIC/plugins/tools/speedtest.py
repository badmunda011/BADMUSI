# Copyright (C) 2024 by Badhacker98@Github, < https://github.com/Badhacker98 >.
# Owner https://t.me/ll_BAD_MUNDA_ll

import asyncio

import speedtest
from pyrogram import filters

from BADMUSIC import app
from BADMUSIC.misc import SUDOERS
from strings import get_command

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("⇆ ʀᴜɴɴɪɴɢ ᴅᴏᴡɴʟᴏᴀᴅ sᴩᴇᴇᴅᴛᴇsᴛ...")
        test.download()
        m = m.edit("⇆ ʀᴜɴɴɪɴɢ ᴜᴘʟᴏᴀᴅ sᴘᴇᴇᴅᴛᴇsᴛ...")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("↻ sʜᴀʀɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("ʀᴜɴɴɪɴɢ sᴘᴇᴇᴅᴛᴇsᴛ")
    loop = asyncio.get_event_loop_policy().get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**sᴘᴇᴇᴅᴛᴇsᴛ ʀᴇsᴜʟᴛ**
    
<u>**ᴄʟɪᴇɴᴛ:**</u>
**ɪsᴘ :** {result['client']['isp']}
**ᴄᴏᴜɴᴛʀʏ :** {result['client']['country']}
  
<u>**sᴇʀᴠᴇʀ :**</u>
**ɴᴀᴍᴇ :** {result['server']['name']}
**ᴄᴏᴜɴᴛʀʏ :** {result['server']['country']}, {result['server']['cc']}
**sᴘᴏɴsᴏʀ :** {result['server']['sponsor']}
**ʟᴀᴛᴇɴᴄʏ :** {result['server']['latency']}  
**ᴘɪɴɢ :** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=result["share"], caption=output
    )
    await m.delete()
