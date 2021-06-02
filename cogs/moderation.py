import discord
from discord.ext import commands


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()  # uses command decorators, in this case inside a cog
    @commands.has_permissions(ban_members=True)  # only people that have permissions to ban users can use this command
    async def ban(self, ctx, user: discord.Member, *, reason):  # The person banning someone has to ping the user to ban, and input a reason. Remove self if you are outside a cog.
        await ctx.guild.ban(user, reason=reason)  # Bans the user.
        await user.send(f"You have been banned in {ctx.guild} for {reason}")  # Private messages user.
        await ctx.send(f"{user} has been successfully banned.")  # messages channel to tell everyone it worked


def setup(bot):
    bot.add_cog(Moderation(bot))
