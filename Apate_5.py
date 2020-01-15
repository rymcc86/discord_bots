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

##------ Events ------##
client = discord.Client()

@client.event
async def on_ready():
        print(f'Joined {GUILD}. The Home of The Thieves Guild.')
        print(f'Bot Ready.')

@client.event
async def on_member_join(member):
        print(f'{member} has joined {GUILD}.')
        channel = client.get_channel(593045340064841739)
        await channel.send(f'Welcome! {member} has joined {GUILD}, Roles will be assigned shortly.')

        for channel in member.guild.channels:
            if str(channel) == "tg-general":
                 GuildGreeting = (f'{member.name}\nWelcome to the Thieves Guild!\n\nTo help you settle in and find all of the information you requiire here\'s some quick info to get you started.\n\nYou can find a quick how-to for the intel bot in the channel #tg-rules-and-info.\n\nActive intel can be found in #tg-ogtheft-and-camping but keep chatter in this channel to a minimum!\n\nAny further questions please do ask the wider group and get to know them, most importantly: STEAL EVERYTHING!!!!!!!\n\n The Guild Always Wins!')
                 await member.create_dm()
                 await member.dm_channel.send(GuildGreeting)

@client.event
async def on_member_remove(member):
        print(f'{member} has left "{GUILD}". Bye Felicia!')
        channel = client.get_channel(593045340064841739)
        await channel.send(f'{member} has left "{GUILD}". Bye Felicia!')

@client.event
async def on_member_update(before,after):
    if before.nick != after.nick and after.nick is not None:
        print(f'{before.display_name} has been updated.')
        print(f'Before:{before.nick} \nAfter:{after.nick}')
        channel = client.get_channel(666596539979792398)
        await channel.send(f'{before.display_name} has been updated.')
        await channel.send(f'Before:{before.nick} \nAfter:{after.nick}')

    if before.roles != after.roles:
        print(f'{before.display_name} has been updated.')
        print(f'Before:{before.roles} \nAfter:{after.roles}')
        channel = client.get_channel(666596539979792398)
        await channel.send(f'{before.display_name} has been updated.')
        await channel.send(f'Before:{before.roles} \nAfter:{after.roles}')

        if len(before.roles) < len(after.roles):
            new_role = next(role for role in after.roles if role not in before.roles)
            if new_role.name in ('Thieves Guild'):
                channel = client.get_channel(476876411349762049)
                await channel.send(f'{after.mention}\n"https://media.giphy.com/media/Ae7SI3LoPYj8Q/giphy.gif"')
#           elif new_role.name in ('___role_name___'):
#               channel = client.get_channel(___Channel_ID___)
#               await channel.send(f'{after.mention}\n___channel_greeting___')

@client.event
async def on_message(message):
        if message.author == client.user:
            return

        if message.content == '99!':
            brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            'I\'ve been trying to catch the Pontiac Bandit for eight years. You know how many months that is?',
            'One of you is a criminal, and the other one is dressed like Steve Harvey',
            'How many cars would you say this Pontiac Bandit has stolen?',
            'Not me, Captain. I was napping',
            'I understand. Just know, you have disappointed all three of us.',
            'You know, the doctor said if the bullet was two millimetres to the left and a foot higher, I might never have walked again',
                (
                'All this cycling makes me feel like Lance Armstrong, '
                'Like you use performance-enhancing drugs and have one testicle?'
                ),
                (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
                ),
            ]
            response = random.choice(brooklyn_99_quotes)
            await message.channel.send(response)

        if message.content == 'Do it!':
            doit = [
            'https://media.giphy.com/media/qDPg6HNz2NfAk/giphy.gif',
            ]

            response = random.choice(doit)
            await message.channel.send(response)

        if message.content == 'Sneaky':
            sneaky = [
            'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
            'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
            'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
            'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
            ]

            response = random.choice(sneaky)
            await message.channel.send(response)

        if message.content == 'Stolen':
            theftcelebration = [
            'https://youtu.be/VP32mAY1bzY',
            'https://media.giphy.com/media/Io2j5ZJBss5Rm/giphy.gif',
            'https://media.giphy.com/media/jzDk3BybZHNBK/giphy.gif',
            'https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif',
            'https://media.giphy.com/media/4sRgvD40CDTeo/giphy.gif',
            ]

            response = random.choice(theftcelebration)
            await message.channel.send(response)

        if message.content == 'StolenTG':
            theftcelebrationTG = [
            'https://youtu.be/VP32mAY1bzY',
            ]

            response = random.choice(theftcelebrationTG)
            await message.channel.send(response)

##---- Bot Commands ----##
bot = commands.Bot(command_prefix = '$')

#--- Maintenance Window Silent Command ---#
#silent_channels = set(['public-chat','tg-general','tg-leadership-events'])



##---- Run ----##
client.run(TOKEN)
