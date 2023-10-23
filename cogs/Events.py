import discord
from discord.ext import commands
from discord import Embed
from discord.ext.commands import CommandNotFound

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client
  
    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Events")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, CommandNotFound):
            em = Embed(description = "**Error! <a:cross:766645598057005077>**\nCommand Not Found!", color = 0x32ddff)
            await ctx.send(embed = em)

                

def setup(client):
    client.add_cog(Events(client))           