import discord, requests, pyfiglet
from discord.ext import commands as VibeBot
from VibeBot.load import token

Output = "VibeBot || "

class Activity(VibeBot.Cog):
    def __init__(self, bot):
        self.bot = bot


    @VibeBot.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message,
            url = "https://www.whatavibe.net/SelfBot", 
        )
        await self.bot.change_presence(activity=stream)    

        
    @VibeBot.command()
    async def playing(self, ctx, *, message):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.bot.change_presence(activity=game)
    
    
    @VibeBot.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name=message, 
            ))
           
            
    @VibeBot.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name=message
            ))


    @VibeBot.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)


def setup(bot):
    bot.add_cog(Activity(bot))