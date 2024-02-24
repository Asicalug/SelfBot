from PyDictionary import PyDictionary
from discord.ext import commands
import datetime
from termcolor import colored

dictionary=PyDictionary

class Dictionary(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")


    @commands.command()
    async def meaning(self, ctx, word: str):
        await ctx.message.delete()
        if word != None:
            try:
                output = await ctx.send(dictionary.meaning(word))
                print(colored('[OUTPUT]', 'yellow'))
                print(f'{self.bot.command_prefix}meaning\n{output.content}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")
            except Exception as error:
                output = await ctx.send(f"```console\n{error}\n```")
                print(colored('[ERROR]', 'red'))
                print(f'{self.bot.command_prefix}meaning\n{error}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")

    @commands.command()
    async def antonym(self, ctx, word: str):
        await ctx.message.delete()
        if word != None:
            try:
                output = await ctx.send(dictionary.antonym(word))
                print(colored('[OUTPUT]', 'yellow'))
                print(f'{self.bot.command_prefix}antonym\n{output.content}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")
            except Exception as error:
                output = await ctx.send(f"```console\n{error}\n```")
                print(colored('[ERROR]', 'red'))
                print(f'{self.bot.command_prefix}antonym\n{error}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")

    @commands.command()
    async def synonym(self, ctx, word: str):
        await ctx.message.delete()
        if word != None:
            try:
                output = await ctx.send(dictionary.synonym(word))
                print(colored('[OUTPUT]', 'yellow'))
                print(f'{self.bot.command_prefix}ping\n{output.content}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")
            except Exception as error:
                output = await ctx.send(f"```console\n{error}\n```")
                print(colored('[ERROR]', 'red'))
                print(f'{self.bot.command_prefix}synonym\n{error}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")

async def setup(bot):
	await bot.add_cog(Dictionary(bot))