import discord
from discord.ext import commands
import random
from helper import Bot
client = discord.Client()
bot = Bot()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!99':
        response = bot.nine_nine()
        await message.channel.send(response)

    if bot.bad_words(message.content):
        await message.delete()


client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvPLpQ.m_4pb8ZDkODhAYDO5vQXa1RqLg0")
