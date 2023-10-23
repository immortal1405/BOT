import discord
import datetime
import typing 
from typing import Optional
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingRequiredArgument

class Embed(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True, case_insensitive = True)
    async def embed(self, ctx, color : discord.Color, *, message):
        em = discord.Embed(description = message, color = color)
        await ctx.message.delete()
        await ctx.send(embed = em)

    @embed.error
    async def embed_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            desc = "<a:cross:766645598057005077>  WRONG SYNTAX\n\n<a:g_done:765209928737751090>  CORRECT SYNTAX\n+embed #32ddff <CORRECT SYNTAX>"
            em = discord.Embed(description = desc, color = 0xe67e22)
            await ctx.send(embed = em)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Embed")

def setup(client):
    client.add_cog(Embed(client))