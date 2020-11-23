""" Author: Monica Luong
Date Created: July 26, 2020
Desc: Discord bot that sends helpful reminders to help you grind.
 Type a command like “rpg hunt” or “rpg training.”
 The bot will register your command and automatically ping you
 when that command is ready to be used again. Not associated with epic rpg
 """
import os
import discord
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    """# hunt
    if message.content.startswith('rpg hunt'):
        await message.channel.send('Hello!')

    # fishing
    elif message.content.startswith('rpg fish'):
        await message.channel.send('Fish is ready ')
    elif message.content.startswith('rpg net'):
        None
    elif message.content.startswith('rpg boat'):
        None
    elif message.content.startswith('rpg bigboat'):
        None

    # chopping
    elif message.content.startswith('rpg chop'):
        None
    elif message.content.startswith('rpg axe'):
        None
    elif message.content.startswith('rpg bowsaw'):
        None
    elif message.content.startswith('rpg chainsaw'):
        None

    # pickup
    elif message.content.startswith('rpg pickup'):
        None
    elif message.content.startswith('rpg ladder'):
        None
    elif message.content.startswith('rpg tractor'):
        None
    elif message.content.startswith('rpg greenhouse'):
        None

    # mining
    elif message.content.startswith('rpg mine'):
        None
    elif message.content.startswith('rpg pickaxe'):
        None
    elif message.content.startswith('rpg drill'):
        None
    elif message.content.startswith('rpg dynamite'):
        None

    # adventure
    elif message.content.startswith('rpg adv'):
        None

    # training
    elif message.content.startswith('rpg tr'):
        None

    # quests
    elif message.content.startswith('rpg quest'):
        None
    elif message.content.startswith('rpg epic quest'):
        None

    # arena
    elif message.content.startswith('rpg arena'):
        None

    # miniboss
    elif message.content.startswith('rpg miniboss'):
        None

    # guild
    elif message.content.startswith('rpg guild raid'):
        None
    elif message.content.startswith('rpg upgrade'):
        None

    # lootbox
    elif message.content.startswith('rpg lootbox'):
        None
    elif message.content.startswith('rpg lb'):
        None

    # dailies, weeklies, voting
    elif message.content.startswith('rpg daily'):
        None
    elif message.content.startswith('rpg weeekly'):
        None
    elif message.content.startswith('rpg vote'):
        None
"""
client.run(BOT_TOKEN)