import discord
import pytz
import datetime
from typing import Optional
from discord import Member
from datetime import datetime, timezone
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context = True, case_insensitive = True)
    async def membercount(self, ctx):
        da = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        date = da.astimezone(tz)
        d = f"**Members**\n{ctx.guild.member_count + 1}"
        em = discord.Embed(description = d, color = ctx.message.author.top_role.color, timestamp = date)
        await ctx.send(embed = em)

    @commands.command(pass_context = True, case_insensitive = True, aliases = ["memberinfo", "ui", "mi"])
    async def userinfo(self, ctx, member : Optional[Member]):
        member = member or ctx.message.author
        da = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        date = da.astimezone(tz)
        em = discord.Embed(title = "<a:g_done:765209928737751090> USERINFO <a:g_done:765209928737751090>", 
                            color = 0x32ddff)
        em.set_author(name=member, icon_url=member.avatar_url)
        em.set_thumbnail(url = member.avatar_url)
        em.set_footer(text = f"ID : {ctx.message.author.id} • Today at {date:%H:%M}")
        fields = [("ID", member.id, False),
                ("NICKNAME", member.nick, False),
                ("JOINED SERVER", member.joined_at.strftime("%H:%M:%S, %b %d, %Y"), False),
                ("JOINED DISCORD", member.created_at.strftime("%H:%M:%S, %b %d, %Y"), False),
                ("BOT", member.bot, False),
                ("HIGHEST ROLE", member.top_role.mention, False)
                ]
        
        for name, value, inline in fields:
            em.add_field(name = name, value = value, inline = inline)

        await ctx.send(embed = em)

    @commands.command(pass_context = True, case_insensitive = True, aliases = ["guildinfo", "si", "gi"])
    @commands.is_owner()
    async def serverinfo(self, ctx):
        da = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        date = da.astimezone(tz)
        guild = ctx.guild
        em = discord.Embed(title = "<a:g_done:765209928737751090> SERVERINFO <a:g_done:765209928737751090>", 
                            color = 0x32ddff)
        em.set_author(name=guild.name, icon_url=guild.icon_url)
        em.set_thumbnail(url = guild.icon_url)
        em.set_footer(text = f"ID : {ctx.message.author.id} • Today at {date:%H:%M}")
        fields = [("ID", guild.id, False),
                ("SERVER OWNER", guild.owner, False),
                ("REGION", guild.region, False),
                ("VERIFICATION", guild.verification_level, False),
                ("MEMBERS", guild.member_count + 1, False),
                ("CATEGORIES", len(guild.categories), False),
                ("TEXT CHANNELS", len(guild.text_channels), False),
                ("VOICE CHANNELS", len(guild.voice_channels), False)
                ]
        
        for name, value, inline in fields:
            em.add_field(name = name, value = value, inline = inline)

        await ctx.send(embed = em)
        

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Info")

def setup(client):
    client.add_cog(Info(client))