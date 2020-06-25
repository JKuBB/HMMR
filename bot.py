import discord
from discord.ext import commands
import random
from helper import Bot

client = discord.Client()
bot = Bot()

@client.event
async def on_message(message):
    global queue

    word_list = message.content.split()
    if message.author == client.user:
        return

    if message.content == '!99':
        response = bot.nine_nine()
        await message.channel.send(response)

    if bot.bad_words(word_list):
        await message.delete()

    if message.content == '=j':
        len = bot.q(message.author.name)
        to_send = f'{message.author.name} has entered the queue.  [{len}/4]'
        if len == 10:
            await message.channel.send("You can't join a queue if you're already in one ;)")
        else:
            await message.channel.send(to_send)

    if message.content == '=l':
        len = bot.dq(message.author.name)
        to_send = f'{message.author.name} has left the queue.  [{len}/4]'
        if len == 10:
            await message.channel.send("You can't leave a queue if you're aren't in one ;)")
        else:
            await message.channel.send(to_send)


client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvPZ3g.PVROZGRRAAXqtMTrdWKuu8913Wg")
