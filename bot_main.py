import discord, os
from dotenv import load_dotenv
from srb2k_bot.sonic_bot import sonic_bot
from srb2k_bot.cogs import *

def main():
    load_dotenv()

    token = os.getenv("TOKEN")
    intents = discord.Intents.default()
    intents.members = True
    intents.guilds = True
        
    bot = sonic_bot(command_prefix='!', intents=intents)

    bot.add_cog(music_player(bot))
    bot.add_cog(main_cog(bot))

    print()
    bot.run(token)

if __name__ == '__main__':
    main()