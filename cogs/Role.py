import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingPermissions, MissingRequiredArgument
from discord import Message, PartialEmoji

class Role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, case_insensitive = True)
    @has_permissions(manage_roles = True)
    async def addrole(self, ctx, member : discord.Member, role : discord.Role):
        if (ctx.message.author.top_role.position >= member.top_role.position):
            await member.add_roles(role)
            embed = discord.Embed(description = f"<a:g_done:765209928737751090>  Changed roles for {member}, + {role.name}", color = 0x32dd32)
            await ctx.send(embed = embed)    
        else:
            em = discord.Embed(description = f"<a:cross:766645598057005077> Check you role position.", color = 0x32dd32)
            await ctx.send(embed = em)

    @commands.command(pass_context=True, case_insensitive = True)
    @has_permissions(manage_roles = True)
    async def removerole(self, ctx, member : discord.Member, role : discord.Role):
        if (ctx.message.author.top_role.position >= member.top_role.position):
            await member.remove_roles(role)
            embed = discord.Embed(description = f"<a:g_done:765209928737751090>  Changed roles for {member}, - {role.name}", color = 0x32dd32)
            await ctx.send(embed = embed)    
        else:
            em = discord.Embed(description = f"<a:cross:766645598057005077> Check you role position.", color = 0x32dd32)
            await ctx.send(embed = em)

    @removerole.error
    async def removerole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            dec = f"<a:cross:766645598057005077>  Its look like you don't have permission to manage roles."
            embed = discord.Embed(description = dec, color = 0xddffdd)
            await ctx.send(embed = embed)

        if isinstance(error, MissingRequiredArgument):
            desc = """<a:cross:766645598057005077>  Please provide all the rquired arguments.\n\n
                Usage -\n
                +removerole @user @role"""
            emb = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = emb)

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to manage roles."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        
        if isinstance(error, MissingRequiredArgument):
            desc = """<a:cross:766645598057005077>  Please provide all the rquired arguments.\n\n
                Usage -\n
                +addrole @user @role"""
            emb = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Role")
        

def setup(client):
    client.add_cog(Role(client))        