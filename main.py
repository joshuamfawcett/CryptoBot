import discord
from discord.ext import commands
import string
import os
import asyncio
import typing
import toml
from art import *
from utils import *

config = toml.load('config.toml')

def command_prefix(bot, message):
    if message.guild is None:
        return ''
    else:
        return config['core']['prefix']

async def get_prefix(ctx):
  return '' if ctx.guild is None else config['core']['prefix']

bot = commands.Bot(command_prefix)
#bot.remove_command('help') # default help command SUCKS


@bot.event
async def on_ready():
  print(f'Logged in as {bot.user}!')
  activity = discord.Game(name=f"Currently on {len(bot.guilds)} servers")
  await bot.change_presence(activity=activity)

@bot.event
async def on_guild_join(self):
	activity = discord.Game(name=f"Currently on {len(bot.guilds)} servers")
	await bot.change_presence(activity=activity)

@bot.event
async def on_guild_remove(self):
	activity = discord.Game(name=f"Currently on {len(bot.guilds)} servers")
	await bot.change_presence(activity=activity)

#print('Loading Help cog...')
#bot.load_extension("cogs.help")

print('Loading Debug cog...')
bot.load_extension("cogs.debug")

print('Loading Caesar cipher cog...')
bot.load_extension("cogs.caesar")

print('Loading Polybius cipher cog...')
bot.load_extension("cogs.polybius")

print('Loading Others cog...')
bot.load_extension("cogs.others")

bot.run(config['core']['token'])
