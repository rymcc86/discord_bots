#Apate_5.py
import os
import discord
import random
from dotenv import load_dotenv
from discord.ext import commands


##---- Env Variables ----##
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

##---- Declare Command Prefix ----##
#client = commands.Bot(command_prefix = '.')
client = discord.Client()


##------ Events ------##
@client.event
async def on_ready():
        print(f'Joined "{GUILD}". The Home of The Thieves Guild.')
        print(f'Bot Ready.')

@client.event
async def on_member_join(member):
        print(f'{member} has joined "{GUILD}".')
        channel = client.get_channel()
        await channel.send(f'{member} has joined "{GUILD}".')

@client.event
async def on_member_remove(member):
        print(f'{member} has left "{GUILD}". Bye Felicia!')

@client.event
async def on_member_update(before,after):
    if before.nick != after.nick and after.nick is not None:
        print(f'{before.display_name} has been updated.')
        print(f'Before:{before.nick} \nAfter:{after.nick}')
    if before.roles != after.roles:
        print(f'{before.display_name} has been updated.')
        print(f'Before:{before.roles} \nAfter:{after.roles}')

#@client.event
#async def on_member_join(member):
#        await member.create_dm()
#        await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')


@client.event
async def on_message(message):
        if message.author == client.user:
            return

            brooklyn_99_quotes = ['I\'m the human form of the 💯 emoji.']
                    
        if message.content == '99!':
            response = random.choice('brooklyn_99_quotes')
            await message.channel.send(response)


##---- Run ----##
client.run(TOKEN)
