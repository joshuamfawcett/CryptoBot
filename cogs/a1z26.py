from discord.ext import commands
import string

def a1z26(message):

	alphabets=list(string.ascii_lowercase)
	cont=message
	encrypt=''
	num_list=[]
	for i in cont[0:]:
		encrypt=encrypt  + str(i) + " "
		try:
			num_list.append(int(i))
		except:
			pass
	decrypt=''
	if cont[0].isalpha():
		for i in encrypt:
			try:
				z=i.lower()
				decrypt=decrypt+' '+str(alphabets.index(z)+1)
			except:
				decrypt=decrypt+str(i)
	else:
		for i in num_list:
			decrypt=decrypt + " " + str(alphabets[i-1])
	return decrypt


class A1z26(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['number'])
	async def a1z26(self, ctx,*arg):
		await ctx.send(f'```{a1z26(arg)}```')

def setup(bot):
	bot.add_cog(A1z26(bot))