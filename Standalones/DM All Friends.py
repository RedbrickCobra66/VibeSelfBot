import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore


intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="-", intents=intents, self_bot=True)

token = "Token-Here"

@bot.event
async def on_ready():
    message = "http://discord.whatavibe.net/"
    print(f"""{Fore.RED}Basic DM all friends made by bot.whatavibe.net!""")
    for user in bot.user.friends:
        if user.id == bot.user.id:
            pass
        else:
            try:
                await user.send(message)
                await asyncio.sleep(1)
            except:
                print(f"Couldn't interact with {user}")


bot.run(token,bot=False)
