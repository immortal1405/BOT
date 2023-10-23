import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, has_role, MissingPermissions, MissingRequiredArgument

class Create(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='create-category', pass_context = True, case_insensitive = True)
    @has_permissions(administrator=True)
    async def create_category(self, ctx, *, category_name):  
        guild = ctx.guild
        print(f'Creating a new channel: {category_name}')
        overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        await guild.create_category(category_name, overwrites=overwrites)
        await ctx.message.add_reaction("<a:gtick:765208196620222484>")
        embed = discord.Embed(description = f"{ctx.message.author.mention}, The category has been created successfully.", color = ctx.message.author.top_role.color)
        await ctx.send(embed = embed) 

    @commands.command(name='create-channel', pass_context = True, case_insensitive = True)
    @has_permissions(administrator=True)
    async def create_channel(self, ctx, *, channel_name=None):
        guild = ctx.guild
        print(f'Creating a new channel: {channel_name}')
        overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        await guild.create_text_channel(channel_name, overwrites=overwrites)
        await ctx.message.add_reaction("<a:gtick:765208196620222484>")
        embed = discord.Embed(description = f"{ctx.message.author.mention}, The channel has been created successfully.")
        await ctx.send(embed = embed)  

    @commands.command(name='create-vc', pass_context = True, case_insensitive = True)
    @has_permissions(administrator=True)
    async def create_vc(self, ctx, *, vc_name=None):
        guild = ctx.guild
        print(f'Creating a new voice channel: {vc_name}')
        overwrites = {guild.default_role: discord.PermissionOverwrite(view_channel=False)}
        await guild.create_voice_channel(vc_name, overwrites=overwrites)
        await ctx.message.add_reaction("<a:gtick:765208196620222484>")
        embed = discord.Embed(description = f"{ctx.message.author.mention}, The voice channel has been created successfully.", color = ctx.message.author.top_role.color)
        await ctx.send(embed = embed)  

    @commands.command(name = "create-role", pass_context = True, case_insensitive = True)
    @has_permissions(administrator=True)
    async def create_role(self, ctx, *, role_name):
        guild = ctx.guild
        perms = discord.Permissions(send_messages=True, read_messages=True, read_message_history=True)
        await guild.create_role(name=role_name, permissions=perms)
        embed = discord.Embed(description = f"{ctx.author.mention}, The new role has been created as `{role_name}`", color = ctx.message.author.top_role.color)
        await ctx.send(embed = embed)

    @create_role.error
    async def create_role_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to create role."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments.\n\n
                Usage -\n
                +create-role <role_name>"""
            emb = discord.Embed(description = de, color=0xddffdd)
            await ctx.send(embed = emb)

    @create_category.error
    async def create_category_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to create category."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments.\n\n
                Usage -\n
                +create-category <category_name>"""
            emb = discord.Embed(description = de, color=0xddffdd)
            await ctx.send(embed = emb)

    @create_channel.error
    async def create_channel_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to create text channelk."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments.\n\n
                Usage -\n
                +create-channel <channel_name>"""
            emb = discord.Embed(description = de, color=0xddffdd)
            await ctx.send(embed = emb)

    @create_vc.error
    async def create_vc_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            desc = f"<a:cross:766645598057005077>  Its look like you don't have permission to create channels."
            embed = discord.Embed(description = desc, color = 0xddffdd)
            await ctx.send(embed = embed)
        if isinstance(error, MissingRequiredArgument):
            de = """<a:cross:766645598057005077>  Please provide all the required arguments.\n\n
                Usage -\n
                +create-vc <vc_name>"""
            emb = discord.Embed(description = de, color=0xddffdd)
            await ctx.send(embed = emb)

    @commands.Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("Create")

def setup(client):
    client.add_cog(Create(client))        