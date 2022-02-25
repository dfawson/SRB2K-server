from clients.sonic_bot import sonic_bot
import discord
from cogs.main_cog import main_cog
from cogs.play_music import music_player

def main():
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
        
    bot = sonic_bot(command_prefix='!', intents=intents)

    bot.add_cog(music_player(bot))
    bot.add_cog(main_cog(bot))

    bot.run("OTQ2MTgyNjc2Nzk1MjMyMjg2.Yha_SQ.Jap4NMeb_O4oqIkHtCqXlqWxUIM")

if __name__ == '__main__':
    main()