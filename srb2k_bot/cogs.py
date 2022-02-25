import discord, random, asyncio, os
from discord.ext import commands

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




class music_player(commands.Cog, name='music player module'):
    #gets music

    def __init__(self, bot):
        self.bot = bot
        self.queue = []
        self.playlists = {"outer wilds" : ["14.3 billion years", "a dream of home", "echoes of the eye", "end of the wilds", "end times", "outer wilds", "river's end", "the ash twin project", "the lost waltz", "the museum", "the river", "the sound of water", "timber hearth", "travelers"]}
        self.vc = None
        self.dir = os.getcwd()

    @commands.command(name="play")
    async def queue_song(self,ctx,arg1=None,arg2=None):
        print(arg1,arg2)
        if ctx.author.voice == None:
            await ctx.send('you gotta be in a channel to play music.')
            return

        if arg1 == None:
            if self.vc != None and self.vc.is_paused():
                self.vc.resume()
                return
            await ctx.send("please enter a playlist.")
            return

        if arg1 not in self.playlists.keys():
            await ctx.send("we don't have that playlist.")
            return

        if arg2 == None:
            shuffle_list = self.playlists[arg1]
            random.shuffle(shuffle_list)
            for item in shuffle_list:
                self.queue.append('/home/pi/SRB2K-server/srb2k_bot/playlists/{0}/{1}.mp3'.format(arg1,item))
        elif arg2 not in self.playlists[arg1]:
            await ctx.send("I don't know that song.")
            return
        else:
            self.queue.append('/home/pi/SRB2K-server/srb2k_bot/playlists/{0}/{1}.mp3'.format(arg1,item))
        
        voice_channel = ctx.author.voice.channel
        print(voice_channel)
        if self.vc == None:
            self.vc = await voice_channel.connect()
            while len(self.queue) > 0:
                print(self.queue[0])
                audio_source = discord.FFmpegPCMAudio(self.queue[0])
                print(self.vc)
                print(audio_source)
                self.vc.play(audio_source)
                print(self.vc.is_connected())
                while self.vc.is_playing() or self.vc.is_paused():
                    await asyncio.sleep(1)
                self.queue.pop(0)
            self.vc.stop()
            await self.vc.disconnect()
            self.vc = None

    #pauses the music
    @commands.command(name='pause')
    async def pause_song(self,ctx):
        if self.vc == None:
            await ctx.send('nothing is playing.')
            return
        self.vc.pause()
    
    #clears the queue and stops the music
    @commands.command(name='stop')
    async def stop_song(self,ctx):
        if self.vc == None:
            await ctx.send('nothing is playing.')
            return
        #sets queue to length of one so pop function in the main command doesn't throw up error
        self.queue = [None]
        self.vc.stop()
    
    #skips current song
    @commands.command(name='skip')
    async def skip_song(self,ctx):
        if self.vc == None:
            await ctx.send('nothing is playing.')
            return
        self.vc.stop()
        