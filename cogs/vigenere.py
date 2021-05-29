from discord.ext import commands
import string

alphabet = string.ascii_lowercase
alphabet_upper = alphabet.upper()

def vigenere(text, key, mode):
    if key != None and text != None:
        lowercase = text.lower()
        encrypted = ''
        index = None
        counter = 0
        alphabet = string.ascii_lowercase
        alphabet_upper = alphabet.upper()
        # First do the shifting thingy
        for char in lowercase:
            # Make sure the index does not exceed the key's length
            if counter == len(key): counter = 0

            if char not in alphabet:
                encrypted += char
            else:
                index = alphabet.index(char)

                if mode == 'encrypt':
                    index += alphabet.index(key[counter])
                else:
                    index -= alphabet.index(key[counter])

                index %= len(alphabet)
                encrypted += alphabet[index]
                counter += 1

        # Restore cases
        for x in range(len(encrypted)):
            encrypted = list(encrypted)
            if text[x] in alphabet_upper:
                encrypted[x] = encrypted[x].upper()

        return ''.join(encrypted)
    else:
        response = "You have not entered the key or the code. Please enter the command with the key as well as the text to be decoded/encoded"
        return response


class Vigenere(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def vigenere_decode(self, ctx, key, *, arg):
        await ctx.send(f"```{vigenere(arg, key, 'decrypt')}```")

    @commands.command()
    async def vigenere_encode(self, ctx, key=None, *, arg=None):
        await ctx.send(f"```{vigenere(arg, key, 'encrypt')}```")


def setup(bot):
    bot.add_cog(Vigenere(bot))
