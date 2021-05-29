from discord.ext import commands
import typing


def caesar(text, s):
    if s != None:
        result = ""
        s = 26 - s
        for i in range(0, len(text)):
            char = text[i]
            if char.isalpha():
                if char != " ":
                    if (char.isupper()):
                        result += chr((ord(char) + s - 65) % 26 + 65)

                    else:
                        result += chr((ord(char) + s - 97) % 26 + 97)
                else:
                    result = result + char
            else:
                result += char
        return result
    else:
        output_l = []
        for i in range(1, 26):
            decrypt = caesar(text, i)
            output_l.append(f"Key = {i}: {decrypt}")
        outp = ''
        for i in output_l:
            outp = outp + i + "\n"
        return outp


class Caesar(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def caesar(self, ctx, key: typing.Optional[int] = None, *, arg):
		await ctx.send(f"```{caesar(arg, key)}```")


def setup(bot):
	bot.add_cog(Caesar(bot))
