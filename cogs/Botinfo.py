import discord
import datetime
from discord.ext import commands
from datetime import datetime

class Botinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True, case_insensitive = True)    
    async def invite(self, ctx):
        embed = discord.Embed(title = "Here is the invite link!", description = "<a:g_done:765209928737751090> Click [here](https://discord.com/api/oauth2/authorize?client_id=750590034721374208&permissions=8&scope=bot) to add me.", color = 0x0000ff)
        await ctx.send(embed = embed)

    @commands.command(pass_context=True, case_insensitive=True)
    async def servers(self, ctx):
        desc = f"<a:rockstar:765933168720740362><a:gtick:765208196620222484>The bot is in " + str(len(self.client.guilds)) + " servers.<a:gtick:765208196620222484><a:rockstar:765933168720740362>"
        embed = discord.Embed(description = desc, color = ctx.message.author.top_role.colour)
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Botinfo")

def setup(client):
    client.add_cog(Botinfo(client))         