import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NjY0MjE2Njc5MzUzNDE3NzUz.XhUWNw.v5KOWLxN0sj4omAvS2bJm4rcQ70')
