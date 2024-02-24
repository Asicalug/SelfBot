import os
import sys
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands.misc.ping import Ping
import asyncio
import inspect

bot = commands.Bot(command_prefix='..', self_bot=True)
bot.startTime = time.time()
def system(type):  # Android, iOS, Client, and Web
  ws = discord.gateway.DiscordWebSocket
  exec(inspect.getsource(ws.identify).replace('payload = {', f'presence["status"] = "afk"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["browser_user_agent"] = "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/15E148 Safari/604.1"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["browser_version"] = "16.5"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["os_version"] = "17"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["browser"] = "Discord {type}"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["device"] = "Discord {type}"\n\x20\x20\x20\x20\x20\x20\x20\x20self._super_properties["os"] = "{type}"\n\x20\x20\x20\x20\x20\x20\x20\x20payload = ' + '{')[4:] + "\nws.identify = identify", {'ws': ws, 'sys': sys, '_log': discord.gateway._log})

system('iOS')

load_dotenv()
TOKEN = os.getenv("TOKEN")
if TOKEN == None:
    print("TOKEN not found in the .env file.")
    exit()

async def load_cogs():
    print("Loading commands")
    try:
        #admin
        await bot.load_extension('commands.admin.reload')

        #misc
        await bot.load_extension("commands.misc.dictionary")
        await bot.load_extension("commands.misc.nitroSniper")
        await bot.load_extension("commands.misc.ping")
        await bot.load_extension("commands.misc.uptime")
        await bot.load_extension("commands.misc.weather")

        print("Commands loaded")
    except Exception as e:
        print(f"could not load {e}")
        pass

asyncio.run(load_cogs())

bot.run(TOKEN)