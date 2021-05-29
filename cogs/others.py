from discord.ext import commands
import discord
from utils import *

class others(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def reverse(self, ctx,*, arg):
      await ctx.send(f'```{arg[::-1]}```')

    @commands.command()
    async def base64_decode(self, ctx ,*, arg):
        await ctx.send(f'```{base64(arg, "decode")}```')

    @commands.command()
    async def base64_encode(self, ctx,*, arg):
        await ctx.send(f'```{base64(arg, "encode")}```')


    @commands.command()
    async def tap(self, ctx,*, arg):
        await ctx.send(f'```{tap(arg)}```')

    @commands.command()
    async def beep(self, ctx):
        await ctx.send('''[Beep beep I'm a sheep](https://www.youtube.com/watch?v=CZlfbep2LdU)''')

def setup(bot):
    bot.add_cog(others(bot))
