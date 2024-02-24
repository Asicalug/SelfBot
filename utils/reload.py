import discord
from discord.ext import commands
from termcolor import colored

class RELOAD:
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def reload(self):
        print('Reloading commands')
        try:
            #admin
            await self.bot.reload_extension('commands.admin.reload')

            #misc
            await self.bot.reload_extension("commands.misc.dictionary")
            await self.bot.reload_extension("commands.misc.nitroSniper")
            await self.bot.reload_extension("commands.misc.ping")
            await self.bot.reload_extension("commands.misc.uptime")
            await self.bot.reload_extension("commands.misc.weather")
            print('Reloaded commands')
        except Exception as error:
            print(colored('[ERROR]', "red"))
            print(error)