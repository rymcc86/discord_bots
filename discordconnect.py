# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('NjY0MjE2Njc5MzUzNDE3NzUz.XhUWNw.v5KOWLxN0sj4omAvS2bJm4rcQ70')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
