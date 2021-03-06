import discord
from discord.ext import commands
import toml
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


config = toml.load('config.toml')

owner_id = config['core']['owner']


def command_prefix(bot, message):
    if message.guild is None:
        return ''
    else:
        return config['core']['prefix']


async def get_prefix(ctx):
    return '' if ctx.guild is None else config['core']['prefix']


bot = commands.Bot(command_prefix)


# bot.remove_command('help') # default help command SUCKS


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')
    print('Bot ID:', bot.user.id)
    print('Discord.py Version:', discord.__version__)
    print('-----------------------')
    print('Servers connected to:')
    for guild in bot.guilds:
        print('-', guild.name)
    print('-----------------------')
    activity = discord.Game(name=f"Currently in {len(bot.guilds)} servers")
    await bot.change_presence(activity=activity)


@bot.event
async def on_guild_join(self):
    activity = discord.Game(name=f"Currently in {len(bot.guilds)} servers")
    await bot.change_presence(activity=activity)


@bot.event
async def on_guild_remove():
    activity = discord.Game(name=f"Currently in {len(bot.guilds)} servers")
    await bot.change_presence(activity=activity)


print("""
  ______                             ______             
 / _____)                  _        (____  \       _    
| /       ____ _   _ ____ | |_  ___  ____)  ) ___ | |_  
| |      / ___) | | |  _ \|  _)/ _ \|  __  ( / _ \|  _) 
| \_____| |   | |_| | | | | |_| |_| | |__)  ) |_| | |__ 
 \______)_|    \__  | ||_/ \___)___/|______/ \___/ \___)
              (____/|_|                                 
""")
print("Version:", config['core']['version'])

# print('Loading Help cog...')
# bot.load_extension("cogs.help")

print('Loading Debug cog...')
bot.load_extension("cogs.debug")

#print('Loading Music cog...')
#bot.load_extension("cogs.music")

print('Loading Moderation cog...')
bot.load_extension("cogs.moderation")

print('Loading Others cog...')
bot.load_extension("cogs.others")

print('Loading UserInfo cog...')
bot.load_extension("cogs.userinfo")

print('Loading Atbash cipher cog...')
bot.load_extension("cogs.atbash")

print('Loading Caesar cipher cog...')
bot.load_extension("cogs.caesar")

print('Loading Morse cipher cog...')
bot.load_extension("cogs.morse")

print('Loading A1z26 cipher cog...')
bot.load_extension("cogs.a1z26")

print('Loading Polybius cipher cog...')
bot.load_extension("cogs.polybius")

print('Loading Vigenere cipher cog...')
bot.load_extension("cogs.vigenere")

print('-----------------------')

bot.run(config['core']['token'])
