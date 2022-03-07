import discord, requests, pyfiglet
from discord.ext import commands as VibeBot

class emoticons(VibeBot.Cog):
    def __init__(self, bot):
        self.bot = bot


    @VibeBot.command()
    async def listemoticons(self, ctx):
        await ctx.message.delete()
        text = "fuckyou, lenny, what, bear, worried, ak47, awp, lmg, sword, love, goodnight, smile"
        await ctx.send(text)

    @VibeBot.command()
    async def fuckyou(self, ctx):
        await ctx.message.delete()
        middle = '╭∩╮(･◡･)╭∩╮'
        await ctx.send(middle)

    @VibeBot.command()
    async def lenny(self, ctx):
        await ctx.message.delete()
        lenny = '( ͡° ͜ʖ ͡°)'
        await ctx.send(lenny)

    @VibeBot.command()
    async def what(self, ctx):
        await ctx.message.delete()
        what = '( ʘ̆ ╭͜ʖ╮ ʘ̆ )'
        await ctx.send(what)

    @VibeBot.command()
    async def bear(self, ctx):
        await ctx.message.delete()
        bear = 'ʕ •ᴥ•ʔ'
        await ctx.send(bear)

    @VibeBot.command()
    async def worried(self, ctx):
        await ctx.message.delete()
        worried = '(´･ _･｀)'
        await ctx.send(worried)

    @VibeBot.command()
    async def ak47(self, ctx):
        await ctx.message.delete()
        ak = '︻╦╤─'
        await ctx.send(ak)


    @VibeBot.command()
    async def awp(self, ctx):
        await ctx.message.delete()
        awp = '︻デ═一'
        await ctx.send(awp)

    @VibeBot.command()
    async def lmg(self, ctx):
        await ctx.message.delete()
        lmg = '︻╦̵̵͇̿̿̿̿╤──'
        await ctx.send(lmg)

    @VibeBot.command()
    async def sword(self, ctx):
        await ctx.message.delete()
        sword = 'ס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>'
        await ctx.send(sword)

    @VibeBot.command()
    async def love(self, ctx):
        await ctx.message.delete()
        love = '(๑′ᴗ‵๑)Ｉ Lᵒᵛᵉᵧₒᵤ♥'
        await ctx.send(love)

    @VibeBot.command()
    async def goodnight(self, ctx):
        await ctx.message.delete()
        night = '✩⋆｡ ˚ᎶᎾᎾⅅ ℕᏐᎶℍᎢ⋆｡˚✩'
        await ctx.send(night)

    @VibeBot.command()
    async def smile(self, ctx):
        await ctx.message.delete()
        smile = '˙ ͜ʟ˙'
        await ctx.send(smile)



def setup(bot):
    bot.add_cog(emoticons(bot))
