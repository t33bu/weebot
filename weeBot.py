
import discord
import os
import datetime
from dotenv import load_dotenv
from urlextract import URLExtract

# dictionary of old urls
w_urls = {}

# load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD')

# setup connection
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# events
@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord!')

@client.event
async def on_message(msg):
    username = str(msg.author).split("#")[0]
    message = str(msg.content)

    if msg.author == client.user:
        return    

    extractor = URLExtract()
    urls = extractor.find_urls(message)
    for u in urls: 
        if u in w_urls:
            await msg.channel.send(f'**W!** Posted by {w_urls[u]}')
        else:
            print(f'Added URL {u}')
            w_urls[u] = f'{username} @ {datetime.datetime.now().strftime("%H:%M %d.%m.%Y")}'
        return

# start bot
client.run(TOKEN)
