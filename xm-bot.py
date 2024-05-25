import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ECHO_BOT_ID = int(os.getenv('ECHO_BOT_ID'))

# set intents
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

# initialize
client = discord.Client(intents=intents)

# when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    print(client.user.id)

# when the bot gets a message
@client.event
async def on_message(message):
    # ignore this bot's or echo bot's messages
    if message.author == client.user or \
       message.author.id == ECHO_BOT_ID:
        return
    
    # add "xm"
    possible_messages = []
    possible_messages.append("xm " + message.content)
    possible_messages.append("xm会" + message.content)
    possible_messages.append("羡慕" + message.content)
    possible_messages.append("羡慕会" + message.content)
    possible_messages.append("好羡慕，我怎么不会" + message.content)
    random_message = random.choice(possible_messages)
    
    # send message
    await message.channel.send(random_message)

client.run(BOT_TOKEN)
