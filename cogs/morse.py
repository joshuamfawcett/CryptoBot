from discord.ext import commands

MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}


def morse_encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter.upper()] + ' '
        else:
            cipher += ' / '

    return cipher


def morse_decrypt(message):
    message = message.split()
    morse_dict = dict((v, k) for (k, v) in MORSE_CODE_DICT.items())
    decipher = ''
    for i in message:
        decipher += morse_dict[i]
    return decipher


def morse(message):
    try:
        return morse_decrypt(message)
    except:
        return morse_encrypt(message)


class Morse(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def morse(self, ctx,*, arg):
        await ctx.send(f'```{morse(arg)}```')

def setup(bot):
    bot.add_cog(Morse(bot))
