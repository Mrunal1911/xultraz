import asyncio
import os
from datetime import datetime
from pathlib import Path

from ULTRA import ALIVE_NAME
from ULTRA import bot 
from ULTRA.utils import admin_cmd, load_module, remove_plugin, sudo_cmd
from ULTRA.utils import edit_or_reply as eor

DELETE_TIMEOUT = 3
thumb_image_path = "./Resources/sinx.jpg"
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "✙ 𝐒𝐢𝐧𝐗 ✙"


@bot.on(admin_cmd(pattern=r"send (?P<shortname>\w+)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"send (?P<shortname>\w+)", allow_sudo=True))
async def send(event):
    if event.fwd_from:
        return
    hmm = bot.uid
    message_id = event.message.id
    thumb = thumb_image_path
    input_str = event.pattern_match.group(1)
    the_plugin_file = "./ULTRA/plugins/{}.py".format(input_str)
    if os.path.exists(the_plugin_file):
        start = datetime.now()
        pro = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            allow_cache=False,
            thumb=thumb,
            reply_to=message_id,
        )
        end = datetime.now()
        time_taken_in_ms = (end - start).seconds
        await eor(
            pro,
            f"**==> Pʟᴜɢɪɴ ɴᴀᴍᴇ:** `{input_str}`\n**==> Uᴘʟᴏᴀᴅᴇᴅ ɪɴ:** `{time_taken_in_ms} Sᴇᴄᴏɴᴅs`.\n**==> Uᴘʟᴏᴀᴅᴇᴅ ʙʏ:** `{DEFAULTUSER}`\n",
        )
        await asyncio.sleep(DELETE_TIMEOUT)
        await event.edit("sᴇɴᴛ !!!") #only italic if loaded markdown else it doesn't look grp
    else:
        await eor(event, "𝚂𝙾𝚁𝚁𝚈 : ғɪʟᴇ ɴᴏᴛ ғᴏᴜɴᴅ")


@bot.on(admin_cmd(pattern="install -true"))
@bot.on(sudo_cmd(pattern="install -true", allow_sudo=True))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            downloaded_file_name = (
                await event.client.download_media(  # pylint:disable=E0602
                    await event.get_reply_message(),
                    "ULTRA/plugins/",  # pylint:disable=E0602
                )
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await eor(
                    event,
                    "Plugin successfully installed\n {}".format(
                        os.path.basename(downloaded_file_name)
                    ),
                )
            else:
                os.remove(downloaded_file_name)
                await eor(
                    event,
                    "Error!\nPlugin cannot be installed!\n Or may have been pre-installed.",
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await eor(event, str(e))
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@bot.on(admin_cmd(pattern=r"unload (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"unload (?P<shortname>\w+)$", allow_sudo=True))
async def unload(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        qwe = await eor(event, f" ✙ 𝐒𝐢𝐧𝐗 ✙ Has Successfully unloaded {shortname}")
    except Exception as e:
        await qwe.edit(
            " ✙ 𝐒𝐢𝐧𝐗 ✙ has Successfully unloaded {shortname}\n{}".format(shortname, str(e))
        )


@bot.on(admin_cmd(pattern=r"load (?P<shortname>\w+)$"))
@bot.on(sudo_cmd(pattern=r"load (?P<shortname>\w+)$", allow_sudo=True))
async def load(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        qwe = await eor(event, f"Successfully loaded {shortname}")
    except Exception as e:
        await qwe.edit(
            f" ✙ 𝐒𝐢𝐧𝐗 ✙  could not load {shortname} because of the following error.\n{str(e)}"
        )
