import discord
import typing
from typing import Optional
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingPermissions, MissingRequiredArgument

class Mod(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, case_insensitive = True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, Reason : Optional[str] = "No reason provided."):    
        if (ctx.message.author.top_role.position >= member.top_role.position
            and not member.guild_permissions.administrator):
            await ctx.guild.ban(member, reason=Reason, delete_message_days = 7)
            embed = discord.Embed(description = f"<a:g_done:765209928737751090> **{member}** has been banned.\nReason : {Reason}", color = 0xf3ff00)
            await ctx.send(embed = embed)
        else:
            em = discord.Embed(description = f"<a:cross:766645598057005077> Its look like you are trying to ban a member who has higher role than yours or has admin powers.", color = 0xffff00)
            await ctx.send(embed = em)

    #@commands.command(pass_context=True, case_insensitive = True)
    #@has_permissions(ban_members=True)
    #async def hackban(self, ctx, member : discord.Member, *, Reason : Optional[str] = "No reason provided."):
        #await ctx.guild.ban(member, reason=Reason, delete_message_days = 7)
        #embed = discord.Embed(description = f"<a:g_done:765209928737751090> **{member}** has been banned.\nReason : {Reason}", color = 0xf3ff00)
        #await ctx.send(embed = embed)

    @commands.command(pass_context=True, case_insensitive = True)
    @has_permissions(kick_members=True)     
    async def kick(self, ctx, member : discord.Member):
        if (ctx.message.author.top_role.position > member.top_role.position
            and not member.guild_permissions.administrator): 
            await ctx.guild.kick(member) 
            embed = discord.Embed(description = f'<a:g_done:765209928737751090> **{member}** has been kicked.', color = 0xffff00)  
            await ctx.send(embed=embed)
            print(f"{member} has been kicked from {ctx.guild.name}.") 
        else:
            em = discord.Embed(description = f"<a:cross:766645598057005077> Its look like you are trying to kick a member who has higher role than yours or has admin powers.", color = 0xffff00)
            await ctx.send(embed = em)
            
    @commands.command(pass_context=True, case_insensitive=True)
    @has_permissions(ban_members=True)
    async def unban(self, ctx, member_id, *, reason="No Reason provided."):
        user = await self.client.fetch_user(int(member_id))
        await ctx.guild.unban(user)
        embed = discord.Embed(description = f"<a:g_done:765209928737751090> **{user}** has been unbanned.\nReason : {reason}", color = 0xf3ff00)
        await ctx.send(embed = embed)
        print(f"{user} has been unbanned.")

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to ban users."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required argument.\n\n
                Usage -\n
                +ban @user <optional reason>"""
            em = discord.Embed(description  = de, color =0xf3ff00)
            await ctx.send(embed = em)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to kick users."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)  
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required argument.\n\n
                Usage -\n
                +kick @user"""
            em = discord.Embed(description  = de, color =0xf3ff00)
            await ctx.send(embed = em)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Oof Dude! First get ban members permission."
            emb = discord.Embed(description = desc, color = 0xf3ff00)
            await ctx.send(embed = emb)
        if isinstance(error, MissingRequiredArgument):
            em = discord.Embed(description  = "<a:cross:766645598057005077>  Provide a member id to unban!", color =0xf3ff00)
            await ctx.send(embed = em)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Mod")

def setup(client):
    client.add_cog(Mod(client))
