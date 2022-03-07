import discord, pyfiglet
from discord.ext import commands as VibeBot 

class mass(VibeBot.Cog):
    def __init__(self, bot):
        self.bot = bot

        
    @VibeBot.command()
    async def massreact(self, ctx, emote):
        await ctx.message.delete()
        messages = await ctx.message.channel.history(limit=20).flatten()
        for message in messages:
            await message.add_reaction(emote)
            
                
    @VibeBot.command()
    async def spam(self, ctx, amount:int=None, *, message: str=None):
        await ctx.message.delete()
        for each in range (0, amount):
            await ctx.send(f"{message}")
    

def setup(bot):
    bot.add_cog(mass(bot))