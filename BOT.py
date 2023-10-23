import discord
import os
import random
import aiohttp
import asyncio
import datetime
import time
import sqlite3
from discord import Intents
from asyncio import sleep
from glob import glob
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from random import randint
from discord.ext.commands import has_permissions, has_role, when_mentioned_or
from discord.ext.commands import Bot as BotBase
from datetime import datetime

PREFIX = "+"
OWNER_IDS = [772335742122590208]
VERSION = "0.1.0"

def get_prefix(client, message):
    return when_mentioned_or(PREFIX)(client, message)

class Ready(object):
    def __init__(self):
        for co in os.listdir("./cogs"):
            if co.endswith(".py"):
                cog = co[:-3]
                setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} cog ready.")

    def all_ready(self):
        for co in os.listdir("./cogs"):
            if co.endswith(".py"):
                cog = co[:-3]
        return all([getattr(self, cog)])

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        super().__init__(command_prefix = PREFIX, 
            owner_ids = OWNER_IDS, 
            case_insensitive = True,
            intents = Intents.all()
            )

    def setup(self):
        for co in os.listdir("./cogs"):
            if co.endswith(".py"):
                cog = co[:-3]
                client.load_extension(f"cogs.{cog}")
                print(f"{cog} loaded.")

        print("Setup Complete.")

    def run(self, version):
        self.VERSION = VERSION    

        print("Running Setup...")
        self.setup()

        self.TOKEN = "NzUwNTkwMDM0NzIxMzc0MjA4.X08vcQ.VWNJxj3H3PVAxF_tvJB41ciGLbk"
        super().run(self.TOKEN, reconnect = True)

    async def on_ready(self):
        if not self.ready:

            while not self.cogs_ready.all_ready():
                await sleep(0.5)


            self.ready = True
            print("Bot is online.")
        else:
            print("Bot reconnected")

client = Bot()   

client.run(VERSION)   