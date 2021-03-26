import discord
import os

client = discord.Client()

COMMAND_STRING = 'faerie' + ' '

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello! Glad to see you fired up!')

  if message.content.startswith(COMMAND_STRING):
    msg = message.content.split(COMMAND_STRING)[1]
    await message.channel.send('You sent the message: {}'.format(msg))

client.run(os.environ['TOKEN'])