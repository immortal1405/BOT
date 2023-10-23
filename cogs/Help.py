import discord
import datetime
import pytz
from datetime import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.remove_command("help")

    @commands.command(pass_context=True, case_insensitive=True)
    async def help(self, ctx):
        embed = discord.Embed(title="PY BOT HELP", description="***PREFIX IS +***\n*ALL COMMANDS ARE CASE INSENSITIVE!*", color = ctx.message.author.top_role.colour) 
        da = datetime.now()
        tz = pytz.timezone('Asia/Kolkata')
        date = da.astimezone(tz)
        embed.set_thumbnail(url=f"{self.client.user.avatar_url}")
        embed.add_field(name = "<a:g_done:765209928737751090> SUPPORT", value = ":white_small_square:**Invite** : Provides the invite link of the bot.")
        embed.add_field(name = "<a:g_done:765209928737751090> FUN COMMANDS", value = ":white_small_square:**8ball** : Gives a random answer to your question.\n:white_small_square:**Av** : Gives the avatar of the user you mention.\n:white_small_square:**Embed** : Embeds your message.\n:white_small_square:**Meme** : Responds with a meme.\n:white_small_square:**Ping** : Returns your ping with pong.\n:white_small_square:**Say** : Says your message.\n:white_small_square:**React** : Adds the emoji to the message whose message id has been provided.", inline = False)
        embed.add_field(name = "<a:g_done:765209928737751090> MODERATION COMMANDS", value = ":white_small_square:**Addrole** : Adds the specified role to the user you specified.\n:white_small_square:**Ban** : Bans a user.\n:white_small_square:**Clear/Purge** : Clears the no. of messages that you have mentioned.\n:white_small_square:**Kick** : Kicks the user that you have mentioned.\n:white_small_square:**Mute** : Mutes a user from the chat.\n:white_small_square:**Removerole** : Removes the specified role from the user you specified.\n:white_small_square:**Setnick** : Changes the nickname of the user.\n:white_small_square:**Unban** : Unbans a user.\n:white_small_square:**Unmute** : Mutes a user from the chat.", inline = False)
        embed.add_field(name = "<a:g_done:765209928737751090> ADMIN COMMANDS", value = ":white_small_square:**Create-category** : Creates a category at the bottom of the server.\n:white_small_square:**Create-channel** : Creates a text channel at the top of the server.\n:white_small_square:**Create-role** : Creates a new role.\n:white_small_square:**Create-vc** : Creates a voice channel at the top of the server.", inline = False)
        embed.add_field(name = "<a:g_done:765209928737751090> DEVELOPER COMMANDS", value = ":white_small_square:**Uptime** : Shows the uptime of the bot", inline = False)
        embed.set_footer(text=f"Requested by {ctx.message.author.name} • {date:%d %b} at {date:%H:%M}", icon_url=(f"{ctx.message.author.avatar_url}"))
        await ctx.message.add_reaction("<a:gtick:765208196620222484>")
        await ctx.send(embed=embed)    

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Help")


def setup(client):
    client.add_cog(Help(client))