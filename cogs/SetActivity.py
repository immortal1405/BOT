from apscheduler.triggers.cron import CronTrigger
from discord import Activity, ActivityType
from discord.ext.commands import Cog, command, is_owner, check

class SetActivity(Cog):

    def __init__(self, client):
        self.client = client

        self._message = "watching +help | {users:,} users in {guilds:,} servers."

        client.scheduler.add_job(self.set, CronTrigger(second=0))

    @property
    def message(self):
        return self._message.format(users = len(self.client.users), guilds = len(self.client.guilds))

    @message.setter
    def message(self, value):
        if value.split(" ")[0] not in ("playing", "watching", "listening", "streaming"):
            raise ValueError("<a:cross:766645598057005077> Invalid activity type.")

        self._message = value

    async def set(self):
        _type, _name = self._message.split(" ", maxsplit=1) and self.message.split(" ", maxsplit=1) 

        await self.client.change_presence(activity=Activity(
            name=_name, type=getattr(ActivityType, _type, ActivityType.playing)
        ))

    @command(name="activity", pass_context=True, case_insensitive = True)
    @is_owner()
    async def activity_message(self, ctx, *, text: str):
        self.message = self._message or text
        await self.set()
        await ctx.send("<a:gtick:765208196620222484> Activity settings changed.")

    @Cog.listener()
    async def on_ready(self):
        if not self.client.ready:
            self.client.cogs_ready.ready_up("SetActivity")


def setup(client):
    client.add_cog(SetActivity(client))