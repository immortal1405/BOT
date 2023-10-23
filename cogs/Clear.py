import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingPermissions, MissingRequiredArgument

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True, aliases=['purge'], case_insensitive = True) 
    @has_permissions(manage_messages=True)   
    async def clear(self, ctx, amount : int):
        await ctx.message.delete()
        await ctx.message.channel.purge(limit=amount)
            

    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to manage messages."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)

        if isinstance(error, MissingRequiredArgument):
            desc = f"<a:cross:766645598057005077>  Provide the amount of messages to clear."
            emb = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Clear")


def setup(client):
    client.add_cog(Clear(client))