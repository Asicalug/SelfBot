from discord.ext import commands
import datetime
from termcolor import colored
from PyDictionary import PyDictionary

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")
	
    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()
        output = await ctx.send(f"> Pong! {round(self.bot.latency * 1000, 2)}ms", mention_author=False)
        print(colored('[OUTPUT]', 'yellow'))
        print(f'{self.bot.command_prefix}ping\n{output.content}\n{datetime.datetime.now()}')
        print("________________________________________________________________________________")

async def setup(bot):
	await bot.add_cog(Ping(bot))