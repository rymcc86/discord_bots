# apate_3.py
import os
import random
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Server')
    
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
        ('All this cycling makes me feel like Lance Armstrong, '
            'Like you use performance-enhancing drugs and have one testicle?'
         ),
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    
        response = random.choice(brooklyn_99_quotes)
        await ctx.send(response)

bot.command(name='Stolen')
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
        
@bot.command(name='Doit!')
async def do_it(ctx):
        doit = [
        'https://media.giphy.com/media/qDPg6HNz2NfAk/giphy.gif',
        ]
    
        response = random.choice(doit)
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
    

        

bot.run(TOKEN)
