from discord.ext import commands


class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(
        name='joinvc',
        description='Makes the bot join the voice channel of the person sending the command.'
    )
    async def joinvc(self, ctx):
        channel = ctx.message.author.voice.channel
        await channel.connect()

    @commands.command(
        name='leavevc',
        description='Makes the bot leave the voice channel it is connected to.'
    )
    async def leavevc(self, ctx):
        channel = ctx.message.guild.voice_client
        await channel.disconnect()


def setup(client):
    client.add_cog(Music(client))
