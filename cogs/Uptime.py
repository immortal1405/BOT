import discord
import datetime
import time
import random
from random import randint
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role
from datetime import datetime

launch_time = datetime.utcnow()

class Uptime(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, case_insensitive = True)
    @commands.is_owner()
    async def uptime(self, ctx):
        delta_uptime = datetime.utcnow() - launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24) 
        embed = discord.Embed(title = "〢𒀲╎ UPTIME", description = f"{days} days {hours} hours {minutes} minutes and {seconds} seconds", color = ctx.message.author.top_role.colour)
        await ctx.send(embed=embed)   

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Uptime") 


def setup(client):
    client.add_cog(Uptime(client))        