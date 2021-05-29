from discord.ext import commands
import discord
from utils import *

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.send('''[Beep beep I'm a sheep](https://www.youtube.com/watch?v=CZlfbep2LdU)''')

def setup(bot):
    bot.add_cog(help(bot))
