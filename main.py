import os
import discord
 
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Привет'):
        await message.channel.send('Здарова!')
 
    if message.content.startswith('пока'):
        await message.channel.send('Ага, давай!')
 
 
my_secret = os.environ['TOKEN']
client.run(my_secret)