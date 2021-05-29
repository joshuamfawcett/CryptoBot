# -*- coding: utf-8 -*-

from discord.ext import commands
import discord
import time
import string
import re
import typing
import asyncio
import sys; sys.path.append("..") # Recognize /utils as a package
from utils import *

alphabet = string.ascii_lowercase


class caesar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def caesar(self, ctx, key: typing.Optional[int] = None,*,  arg):

        await ctx.send(f"```{caesar(arg,key)}```")

def setup(bot):
    bot.add_cog(caesar(bot))
