
import os
import time
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ULTRA import ALIVE_NAME, StartTime, CMD_HELP
#from . import legend
from ULTRAX import BOT, PHOTO, VERSION
from ULTRA.utils import admin_cmd, sudo_cmd
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from platform import python_version, uname


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else " β ππ’π§π β"

        
#make by LEGEND X bht mehnat lag gayi yrr but banhi gaya π 
#so credits ke sath kang krna, nhi to tum jante ho apna bhai DMCA hai ππ
#modify by madboy482
@borg.on(admin_cmd(pattern=r"awake"))
@bot.on(sudo_cmd(pattern=r"awake", allow_sudo=True))
async def amireallyalive(awake):
   """ For .awake command, check if the bot is running.  """
   global PHOTO
   if PHOTO:
     tag = borg.uid
#     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f"**β§β§ β ππ’π§π β IS UP AND RUNNING SUCCESSFULLY β§β§**"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "**β₯β₯ πππππ΄πΌ πππ°πππ β₯β₯**\n\n"
     ALIVE_MESSAGE += "β§ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ : `1.19.5`\n\n"
     ALIVE_MESSAGE += f"β§SINπ ππ΄πππΈπΎπ½ : `{VERSION}`\n\n"
#     ALIVE_MESSAGE += f"β§ ππΏππΈπΌπ΄ : {uptm}\n\n"
     ALIVE_MESSAGE += f"β§ πΌπ π±πΎππ : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "β§ πΆππΎππΏ : [SUPPORT](https://t.me/sinx_support)\n\n"
     ALIVE_MESSAGE += f"β§ [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMrunal1911%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FMrunal1911%2FHEROKU) ππΎππ πΎππ½ πΎπΏ [{BOT}](http://github.com/Mrunal1911/xultraz) β§\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   elif PHOTO == None:
     PHOTO = "https://telegra.ph/file/7a2e0dca3bacda9335947.jpg"
     tag = borg.uid
#     uptm = await legend.get_readable_time((time.time() - StartTime))
     ALIVE_MESSAGE= f"**β§β§ β ππ’π§π β IS UP AND RUNNING SUCCESSFULLY β§β§**"
     ALIVE_MESSAGE += "\n\n"
     ALIVE_MESSAGE += "**β₯β₯ πππππ΄πΌ πππ°πππ β₯β₯**\n\n"
     ALIVE_MESSAGE += "β§ ππ΄π»π΄ππ·πΎπ½ ππ΄πππΈπΎπ½ : `1.19.5`\n\n"
     ALIVE_MESSAGE += f"β§ ππ»πππ° π ππ΄πππΈπΎπ½ : `{VERSION}`\n\n"
#     ALIVE_MESSAGE += f"β§ ππΏππΈπΌπ΄ : {uptm}\n\n"
     ALIVE_MESSAGE += f"β§ πΌπ π±πΎππ : [{DEFAULTUSER}](tg://user?id={tag})\n\n"
     ALIVE_MESSAGE += "β§ πΆππΎππΏ : [SUPPORT](https://t.me/sinx_updates)\n\n"
     ALIVE_MESSAGE += f"β§ [π³π΄πΏπ»πΎπ](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2FMrunal1911%2FHEROKU&template=https%3A%2F%2Fgithub.com%2FMrunal1911%2FHEROKU) ππΎππ πΎππ½ πΎπΏ [{BOT}](http://github.com/Mrunal1911/xultraz) β§\n"   
     await awake.delete() 
     await borg.send_file(awake.chat_id, PHOTO,caption=ALIVE_MESSAGE)
   else:
     await awake.edit("Please add right value in ALIVE_PHOTTO var..")

CMD_HELP.update(
    {
        "awake": "Plugin : awake\
    \n\nSyntax : .awake\
    \nFunction : you can set here costom alive pic .set var ALIVE_PHOTTO (Telegraph link)"
    }
)
