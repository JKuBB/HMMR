import discord
from discord.ext import commands
import random
from helper import Bot

client = discord.Client()
bot = Bot()

@client.event
async def on_message(message):

    #turns phrase to list of words
    word_list = message.content.split()
    #prevents infinite loop case
    if message.author == client.user:
        return
    #nine-nine
    if message.content == '!99':
        response = bot.nine_nine()
        await message.channel.send(response)
    #word filter
    if bot.bad_words(word_list):
        await message.delete()
    #sends embedded messages and adds player to queue
    if message.content == '=j':
        len = bot.q(message.author)

        embed = discord.Embed(description=f'{message.author.name} has entered the queue.  **[{len}/4]**', color=0x0fbfcc)

        if len == 10:
            embed = discord.Embed(description="You can't join a queue if you're already in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            if len!=4:
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="Queue is full. Picking teams...", color=0x0fbfcc)
                await message.channel.send(embed=embed)
                await message.channel.send(f'<@{bot.queue[0].id}> <@{bot.queue[1].id}> <@{bot.queue[2].id}> <@{bot.queue[3].id}>')
                #set teams, need to @people and embed the teams in a pretty way
                teams = bot.set_teams()

    #sends embedded messages and removes player from queue
    if message.content == '=l':
        len = bot.dq(message.author)
        embed = discord.Embed(description=f'{message.author.name} has left the queue.  **[{len}/4]**', color=0x0fbfcc)
        #arbitrary return value so it doesn't clash with length of queue
        if len == 10:
            embed = discord.Embed(description="You can't leave a queue if you aren't in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=embed)

    if message.content.startswith() == '=link':
        bot.link_acct(word_list[1], message.author.name)


client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvQ0Nw.80qdkdN5WPCDZTLOWPumvQRAWIo")
