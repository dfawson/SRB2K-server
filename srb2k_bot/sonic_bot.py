import discord
from discord.ext import commands
import random

class sonic_bot(commands.Bot):
    
    async def on_ready(self):
        

        print('We have logged in as {0.user}'.format(self))

        info_channel = self.get_channel(946305379174866964)
        active = discord.Game("Cunkin'")

        await self.change_presence(status=discord.Status.online, activity=active)
        await info_channel.send("Joined!")