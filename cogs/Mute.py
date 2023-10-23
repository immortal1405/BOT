import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingRequiredArgument, MissingPermissions

class Mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, case_insensitive=True)
    @has_permissions(ban_members = True)
    async def mute(self, ctx, user: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await user.add_roles(role)
        embed = discord.Embed(description = f"<a:g_done:765209928737751090>  User has been muted.", color = 0xff0000)
        await ctx.send(embed = embed) 

    @commands.command(pass_context=True, case_insensitive=True)
    @has_permissions(ban_members = True)
    async def unmute(self, ctx, user: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await user.remove_roles(role)
        embed = discord.Embed(description = f"<a:g_done:765209928737751090>  User has been unmuted.", color = 0xff0000)
        await ctx.send(embed = embed)  

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Oof Dude! You can't mute anyone."
            emb = discord.Embed(description = desc, color = 0xf3ff00)
            await ctx.send(embed = emb)
        if isinstance(error, MissingRequiredArgument):
            em = discord.Embed(description  = "<a:cross:766645598057005077>  Mention a user to mute.", color =0xf3ff00)
            await ctx.send(embed = em)   

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Oof Dude! You can't unmute anyone."
            emb = discord.Embed(description = desc, color = 0xf3ff00)
            await ctx.send(embed = emb)
        if isinstance(error, MissingRequiredArgument):
            em = discord.Embed(description  = "<a:cross:766645598057005077>  Mention a user to unmute.", color =0xf3ff00)
            await ctx.send(embed = em)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Mute")

def setup(client):
    client.add_cog(Mute(client))        