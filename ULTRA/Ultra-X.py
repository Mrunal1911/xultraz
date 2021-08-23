#Copyright 2021-2022 SINX BOT
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from ULTRA import ALIVE_NAME, StartTime
from ULTRA.utils import admin_cmd
from ULTRA import bot
from telethon import version
from math import ceil
import json
import random
import re
from telethon import events, errors, custom
import io
from ULTRA.helpers.functions import get_readable_time
import time
import os
import datetime
#importing finished
from ULTRA import botnickname 
BOT = str(botnickname) if botnickname else "✙ 𝐒𝐢𝐧𝐗 ✙"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "✙ 𝐒𝐢𝐧𝐗 ✙"
tim = get_readable_time((time.time() - StartTime))
#pic 👇
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name 👇
ULTRAX = "[✙ 𝐒𝐢𝐧𝐗 ✙](https://t.me/sinx_updates)"
#my bots repo 👇
REPO = "[✙ 𝐒𝐢𝐧𝐗 ✙ REPO](https://github.com/Mrunal1911/xultraz)"
#grpup👇NAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay 🤔
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/sinx_support)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "✙ 𝐒𝐢𝐧𝐗 ✙ вσт ιѕ ση 🔥 ƒιяє 🔥" 
OP = " нєℓℓσ мαѕтєя му ηαмє ιѕ ✙ 𝐒𝐢𝐧𝐗 ✙ вσт ι αм тнє вєѕт υѕєявσт 💝"
EMOJI = "🔥"
