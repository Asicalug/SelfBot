import discord 
from discord.ext import commands
import time
from termcolor import colored
import datetime
from utils.helper import Plural

class Uptime(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def uptime(self, ctx):
        await ctx.message.delete()
        try:
            timeUp = time.time() - self.bot.startTime
            hoursUp = int("{:.0f}".format(timeUp / 3600))
            minutesUp = int("{:.0f}".format((timeUp / 60) % 60))
            secondsUp = int("{:.0f}".format(timeUp % 60))
            output = await ctx.send(f"> Uptime: {Plural(Hour=hoursUp)}, {Plural(Minute=minutesUp)}, {Plural(Second=secondsUp)}", mention_author=False)
            print(colored('[OUTPUT]', 'yellow'))
            print(f'{self.bot.command_prefix}weather\n{output.content}\n{datetime.datetime.now()}')
            print("________________________________________________________________________________")
        except Exception as error:
            output = await ctx.send(f'```console\n{error}\n```')
            print(colored('[ERROR]', 'red'))
            print(f'{self.bot.command_prefix}weather\n{error}\n{datetime.datetime.now()}')
            print("________________________________________________________________________________")

async def setup(bot):
	await bot.add_cog(Uptime(bot))