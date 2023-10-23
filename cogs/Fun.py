import discord
import random
import pytz
import asyncio
import aiohttp
import time
from datetime import datetime
from discord.ext import commands
from random import randint
from discord.ext.commands import has_permissions, has_role, MissingRequiredArgument
from discord import Message, PartialEmoji

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='8ball', pass_context = True, case_insensitive = True)    
    async def _8ball(self, ctx, *, question):
        responses = ['This is certain.',
                'It is decidely so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As i see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outl(ook not so good.',
                'Very doubtful.']
        await ctx.send(f'Question : {question}\nAnswer : {random.choice(responses)}') 

    @commands.command(pass_context=True, case_insensitive=True, aliases = ["avatar"])
    async def av(self, ctx, *, avamember : discord.Member = None):
        if(avamember == None):
            da = datetime.now()
            tz = pytz.timezone('Asia/Kolkata')
            date = da.astimezone(tz)
            embed = discord.Embed(title = f"{ctx.message.author}", description = "**Avatar**", color = ctx.message.author.top_role.colour)
            embed.set_image(url = f"{ctx.message.author.avatar_url}")
            embed.set_footer(text=f"Requested by {ctx.message.author.name} • {date:%d %b} at {date:%H:%M}", icon_url=(f"{ctx.message.author.avatar_url}"))
            await ctx.send(embed=embed)  
        else:
            da = datetime.now()
            tz = pytz.timezone('Asia/Kolkata')
            dated = da.astimezone(tz)
            emb = discord.Embed(title = f"{avamember}", description = "**Avatar**", color = ctx.message.author.top_role.colour)
            emb.set_image(url = f"{avamember.avatar_url}")
            emb.set_footer(text=f"Requested by {ctx.message.author.name} • {dated:%d %b} at {dated:%H:%M}", icon_url=(f"{ctx.message.author.avatar_url}"))
            await ctx.send(embed=emb) 

    @commands.command(pass_context=True)
    async def meme(self, ctx):
        embed = discord.Embed(title=f"{ctx.message.author.name}", description="Here is your meme!", color = ctx.message.author.top_role.colour)

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True, case_insensitive = True)
    async def ping(self, ctx):
        before = time.monotonic()
        message = await ctx.send("Pinging...")
        ping = (time.monotonic() - before) * 1000
        await message.delete()
        embed = discord.Embed(title = "Pong!", description = f":hourglass_flowing_sand: {int(ping)}ms\n\n:heartbeat: {round(self.client.latency * 1000)}ms", color = ctx.message.author.top_role.colour)
        await ctx.send(embed = embed)

    @commands.command()
    async def react(self, ctx, message: Message, emoji: PartialEmoji):
        await message.add_reaction(emoji) 
        await ctx.message.delete()   
        print(f"Reacted {message} with {emoji}.")

    @commands.command(name='say', pass_context = True, case_insensitive = True)    
    async def _say(self, ctx, *, message):
        await ctx.send(f"{message}\n\n-By {ctx.message.author}")
        await ctx.message.delete()

    @react.error
    async def react_error(self, ctx, error):
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments.\n\n
                Usage -\n
                +react <message_id> <emoji>"""
            emb = discord.Embed(description = de, color=0xddffdd)
            await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Fun")  

def setup(client):
    client.add_cog(Fun(client))     