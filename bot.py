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
        len = bot.q(message.author.name)

        embed = discord.Embed(description=f'{message.author.name} has entered the queue.  **[{len}/4]**', color=0x0fbfcc)

        if len == 10:
            embed = discord.Embed(description="You can't join a queue if you're already in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=embed)
            if len == 4:

                """
                This sets the embed to mention the users as part of the message, it's just a test for seeing if this works
                """
                embed = discord.Embed(description="Queue is full. Picking teams...", color=0x0fbfcc)
                embed.addField("Team 1:", {Bot.Queue[0]} + "\n" + {Bot.Queue[1]}, inline = true)
                embed.addField("Team 2:", {Bot.Queue[2]} + "\n" + {Bot.Queue[3]}, inline = true)
                await message.channel.send(embed=embed)
                #set teams, need to @people and embed the teams in a pretty way
                teams = bot.set_teams()

    #sends embedded messages and removes player from queue
    if message.content == '=l':
        len = bot.dq(message.author.name)
        embed = discord.Embed(description=f'{message.author.name} has left the queue.  [{len}/4]', color=0x0fbfcc)
        #arbitrary return value so it doesn't clash with length of queue
        if len == 10:
            embed = discord.Embed(description="You can't leave a queue if you aren't in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=embed)

    if message.content.startswith() == '=link':
        bot.link_acct(word_list[1], message.author.name)


client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvQ0Nw.80qdkdN5WPCDZTLOWPumvQRAWIo")
