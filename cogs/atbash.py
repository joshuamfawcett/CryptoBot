from discord.ext import commands
import string


def atbash(text):
    if text == None:
        response = "You didn't enter the test. Please enter the command with the text"
        return response
    else:
        alphabets = list(string.ascii_lowercase)
        decrypt = ''
        for i in text:
            try:
                decrypt = decrypt + (alphabets[25 - alphabets.index(i.lower())])
            except:
                decrypt = decrypt + str(i)
        return decrypt


class Atbash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def atbash(self, ctx, *, arg=None):
        await ctx.send(f"```{atbash(arg)}```")


def setup(bot):
    bot.add_cog(Atbash(bot))
