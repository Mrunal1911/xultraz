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
BOT = str(botnickname) if botnickname else "β ππ’π§π β"
NAME = str(ALIVE_NAME) if ALIVE_NAME else "β ππ’π§π β"
tim = get_readable_time((time.time() - StartTime))
#pic π
PIC = os.environ.get("ALIVE_PIC")
#op 
uptime = tim
#time = date + time okay
TIME = time.asctime(time.localtime())
#my name π
ULTRAX = "[β ππ’π§π β](https://t.me/sinx_updates)"
#my bots repo π
REPO = "[β ππ’π§π β REPO](https://github.com/Mrunal1911/xultraz)"
#grpupπNAME = "[{MAATER}](tg://user?id={X})"
#yrr isko apne bot me aply krne se pehle mere se pooch lena ok
#aur aage add kruga abhi busy okay π€
global ghanti
X = bot.uid
MASTER = f"[{NAME}](tg://user?id={X})"
GROUP = "[SUPPORT GROUP](https://t.me/sinx_support)"
#itna test h aur aage krte h
#test successful raha ab aage 
ALIVE = "β ππ’π§π β Π²ΟΡ ΞΉΡ ΟΞ· π₯ ΖΞΉΡΡ π₯" 
OP = " Π½ΡββΟ ΠΌΞ±ΡΡΡΡ ΠΌΡ Ξ·Ξ±ΠΌΡ ΞΉΡ β ππ’π§π β Π²ΟΡ ΞΉ Ξ±ΠΌ ΡΠ½Ρ Π²ΡΡΡ ΟΡΡΡΠ²ΟΡ π"
EMOJI = "π₯"
