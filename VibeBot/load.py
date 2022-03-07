import requests, colorama
from colorama import Fore
from discord.ext import commands as VibeBot
from VibeBot.config import auth, prefix, nitro_sniper, giveaway_sniper

colorama.init()

bot = VibeBot.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command('help')

class load:
    def __init__(self):
        global token
        
        token = self.check_token(auth)


 

        @bot.event
        async def on_ready():

            self.load_cogs()
            print(f'''{Fore.RESET}
                       {Fore.LIGHTMAGENTA_EX}╔{Fore.LIGHTBLACK_EX}═══{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}═══{Fore.LIGHTMAGENTA_EX}╗
                       {Fore.LIGHTBLACK_EX}║ {Fore.LIGHTMAGENTA_EX} _      _   ___   ____  ___   ___  _____ {Fore.LIGHTBLACK_EX}║ 
                       {Fore.LIGHTMAGENTA_EX}║ {Fore.MAGENTA}\ \  / | | | |_) | |_  | |_) / / \  | |  {Fore.LIGHTBLACK_EX}║ 
                       {Fore.LIGHTBLACK_EX}║ {Fore.WHITE} \_\/  |_| |_|_) |_|__ |_|_) \_\_/  |_|  {Fore.LIGHTBLACK_EX}║
                       {Fore.LIGHTMAGENTA_EX}╚═{Fore.LIGHTBLACK_EX}══{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}════{Fore.LIGHTMAGENTA_EX}════{Fore.LIGHTBLACK_EX}═══{Fore.LIGHTMAGENTA_EX}╝
                                {Fore.WHITE}Logged in as {Fore.LIGHTMAGENTA_EX}{bot.user}
                             {Fore.WHITE}You are currently in {Fore.LIGHTMAGENTA_EX}{len(list(bot.guilds))}{Fore.WHITE} server(s).
                            {Fore.WHITE}You have {Fore.LIGHTMAGENTA_EX}{len(list(bot.user.friends))}{Fore.WHITE} Friend(s) in friend list.
                   {Fore.WHITE}VibeBot's prefix is {Fore.LIGHTMAGENTA_EX}{prefix}{Fore.WHITE}, for command-list type {Fore.LIGHTMAGENTA_EX}{prefix}help{Fore.WHITE}.
                              {Fore.WHITE}Brought to you by {Fore.LIGHTMAGENTA_EX}WhatAVibe{Fore.RED}!
                                
                                    ''' + Fore.RESET)

        bot.run(token, bot=False)

    def check_token(self, authorization):
        headers = {'Content-Type': 'application/json', 'authorization': authorization}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            token = authorization
            return token
        else:
            print("Check /VibeBot/config.py file to setup auto-login with token (If you have already set token there please make sure token is valid)")
            print("Please insert your token below:")
            token_input = input()
            token = token_input
            return token
    def load_cogs(self):
         # Loading commands
        bot.load_extension("VibeBot.cogs.fun")
        bot.load_extension("VibeBot.cogs.main")
        bot.load_extension("VibeBot.cogs.activity")
        bot.load_extension("VibeBot.cogs.text_encoding")
        bot.load_extension("VibeBot.cogs.mass")
        bot.load_extension("VibeBot.cogs.currency")
        bot.load_extension("VibeBot.cogs.emoticons")
        bot.load_extension("VibeBot.cogs.nsfw")
        # Loading events
        bot.load_extension("VibeBot.events.on_message")
