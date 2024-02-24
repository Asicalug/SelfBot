from pyowm.owm import OWM
import discord
from discord.ext import commands
import time
import datetime
from termcolor import colored

owm = OWM('4c104a23b4c109deb437dcfb13b3b0c0')

class Weather(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        print(f"{self.__class__.__name__} loaded")

    @commands.command()
    async def weather(self, ctx, city: str, country: str):
        if len(country) != 2:
            output = await ctx.send('country needs to have 2 characters.')
            print(colored('[OUTPUT]', 'yellow'))
            print(f'{self.bot.command_prefix}weather\n{output.content}\n{datetime.datetime.now()}')
            print("________________________________________________________________________________")
        else:
            try:
                mgr = owm.weather_manager()
                weather = mgr.weather_at_place(f'{city},{country}').weather
                temperature_celsius = weather.temperature('celsius')
                output = await ctx.send(f"\nCurrent Temperature: {temperature_celsius['temp']}\nMax Temperature: {temperature_celsius['temp_max']}\nMin Temperature: {temperature_celsius['temp_min']}")
                print(colored('[OUTPUT]', 'yellow'))
                print(f'{self.bot.command_prefix}weather\n{output.content}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")
            except Exception as error:
                await ctx.send(f'```console\n{error}\n```')
                print(colored('[ERROR]', 'red'))
                print(f'{self.bot.command_prefix}weather\n{error}\n{datetime.datetime.now()}')
                print("________________________________________________________________________________")

async def setup(bot):
	await bot.add_cog(Weather(bot))