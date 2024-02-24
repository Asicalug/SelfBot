import os
import sys
import datetime
from termcolor import colored
from discord.ext import commands
from utils.reload import RELOAD

class Reload(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def reload(self, ctx):
        await ctx.message.delete()
        msg = await ctx.send('Restarting...')
        print(f'A "reload" has been requested at {datetime.datetime.now()}')
        try:
           await RELOAD.reload(self)
           await msg.delete()
           await ctx.send('Restarted !')
           
           print(f'Reload successful!')
        except Exception as error:
            output = await ctx.send(f"```console\n{error}\n```")
            print(colored('[OUTPUT]', 'yellow'))
            print(f'{self.bot.command_prefix}ping\n{output.content}\n{datetime.datetime.now()}')
            print("________________________________________________________________________________")

async def setup(bot):
	await bot.add_cog(Reload(bot))