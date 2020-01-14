import os
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = commands.Bot(command_prefix = '.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

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

@client.command(name='chlist')
async def channel_list(ctx):
        response = get_all_channels()
        await ctx.send(response)

@bot.command(name='99')
async def nine_nine(ctx):
        brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'I\'ve been trying to catch the Pontiac Bandit for eight years. You know how many months that is?',
        'One of you is a criminal, and the other one is dressed like Steve Harvey',
        'How many cars would you say this Pontiac Bandit has stolen?',
        'Not me, Captain. I was napping',
        'I understand. Just know, you have disappointed all three of us.',
        'You know, the doctor said if the bullet was two millimetres to the left and a foot higher, I might never have walked again',
         ('All this cycling makes me feel like Lance Armstrong, \n'
            'Like you use performance-enhancing drugs and have one testicle?'
          ),
           (
         'Cool. Cool cool cool cool cool cool cool, '
        'no doubt no doubt no doubt no doubt.'
           ),
        ]

        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)

@bot.command(name='Doit!')
async def do_it(ctx):
        doit = [
        'https://media.giphy.com/media/qDPg6HNz2NfAk/giphy.gif',
        ]

        response = random.choice(doit)
        await ctx.send(response)

@bot.command(name='Stolen')
async def Stolen(ctx):
        theftcelebration = [
        'https://youtu.be/VP32mAY1bzY',
        'https://media.giphy.com/media/Io2j5ZJBss5Rm/giphy.gif',
        'https://media.giphy.com/media/jzDk3BybZHNBK/giphy.gif',
        'https://media.giphy.com/media/5VKbvrjxpVJCM/giphy.gif',
        'https://media.giphy.com/media/4sRgvD40CDTeo/giphy.gif',
        ]

        response = random.choice(theftcelebration)
        await ctx.send(response)

@bot.command(name='StolenTG')
async def Stolen_TG(ctx):
        theftcelebrationTG = [
        'https://youtu.be/VP32mAY1bzY',
        ]

        response = random.choice(theftcelebrationTG)
        await ctx.send(response)

@bot.command(name='SneakySneaky')
async def sneaky_sneaky(ctx):
        sneaky = [
        'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
        'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
        'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
        'https://media.giphy.com/media/ha5EeXrfx3xxC/giphy.gif',
        ]

        response = random.choice(sneaky)
        await ctx.send(response)

client.run(TOKEN)
