import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingPermissions, MissingRequiredArgument

class Setnick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, case_insensitive=True)
    @has_permissions(manage_nicknames=True)
    async def setnick(self, ctx, member: discord.Member, *, nick):
        if (ctx.message.author.top_role.position >= member.top_role.position):
            await member.edit(nick=nick)
            embed = discord.Embed(description = f"<a:g_done:765209928737751090>  Nickname Changed.", color = 0x32ddff)
            await ctx.send(embed = embed)  
        else: 
            em = discord.Embed(description = f"<a:cross:766645598057005077> Please check role positions.", color = 0xffff00)
            await ctx.send(embed = em)  

    @setnick.error
    async def setnick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to manage nicknames."
            em = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = em)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments\n\n
                Usage -\n
                +setnick @user <nickname>"""
            emb = discord.Embed(description = de, color = 0xddffdd) 
            await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Setnick")


def setup(client):
    client.add_cog(Setnick(client))        