# apate_2.py
import os

import discord
from dotenv import load_dotenv

TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'{member.name}, Welcome to the end fuckface!'
    )

client.run(token)
