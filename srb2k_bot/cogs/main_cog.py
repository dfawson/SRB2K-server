import discord
from discord.ext import commands
import random

class main_cog(commands.Cog, name='Main module'):
    def __init__(self,bot):
        self.bot = bot
        self.welcome_messages = ["@everyone \n ***SKRRRT!**** %s drifts in!", "@everyone \n yo whaddup %s.", "@everyone \n Please clear the way for their majesty %s.", "@everyone \n There are some who call them... %s!", "@everyone \n %s finally managed to show up!", "@everyone \n %s is here. Guess the party's ruined.", "@everyone \n %s is here. Time for the party to get started!", "@everyone \n Welcome to the land of the living, %s!"]

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author == self.bot.user:
            return

        if "<:Bupic:946178336487505920>" in message.content and random.randint(1, 100) == 1:
            await message.channel.send("who's that handsome devil?")
        
        if "bup" in message.content.lower():
            bup = self.bot.get_emoji(946530683424231434)
            await message.add_reaction(bup)

    @commands.Cog.listener()
    async def on_member_join(self,member):
        guild = self.bot.get_guild(946174516407730246)
        welcome_channel = self.bot.get_channel(946175477087875082)
        default_role = guild.get_role(946178886251741214)
        await welcome_channel.send(random.choice(self.welcome_messages) %(str(member.mention)))
        await member.add_roles(default_role)
        print('%s has joined.' %(member))