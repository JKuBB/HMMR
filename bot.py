import discord
import random
from helper import Bot
#upon linking, rank channels need to be accessible only by those in said ranks
#updates and database hits
#ADD ERROR MESSAGES FOR COMMANDS AND A PROPER COMMAND LIST
client = discord.Client()
bot = Bot()
#gets info from last time bot was online
bot.create()


@client.event
async def on_message(message):

    #turns phrase to list of words
    word_list = message.content.split()
    #prevents infinite loop case
    if message.author == client.user:
        return
    #nine-nine

    if message.content.lower().strip() == "!david":
        embed = discord.Embed(description="L O L **N 0 0 B**", color=0x0fbfcc)
        await message.channel.send(embed=embed)

    if message.content == '!99':
        response = bot.nine_nine()
        await message.channel.send(response)


    #word filter
    if bot.bad_words(word_list):
        await message.delete()


    #sends embedded messages and adds player to queue
    if message.content.strip().lower() == '=j':
        #NEED A QUEUE TIMEOUT
        len = bot.q(message.author)

        embed = discord.Embed(description=f'{message.author.name} has entered the queue.  **[{len}/4]**', color=0x0fbfcc) #out of 6 for 6mans

        if len == 10:
            embed = discord.Embed(description="You can't join a queue if you're already in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            if len!=4:#or !6 for 6mans
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="Queue is full. Picking teams...", color=0x0fbfcc)
                await message.channel.send(embed=embed)
                await message.channel.send(f'<@{bot.queue[0].id}> <@{bot.queue[1].id}> <@{bot.queue[2].id}> <@{bot.queue[3].id}>') #'''<@{bot.queue[4].id}> <@{bot.queue[5].id}> for 6mans'''
                #set teams, need to @people and embed the teams in a pretty way
                teams = bot.set_teams()
                #create voice channels, and captain selection for teams



    if message.content.strip().lower().startswith("=vote"):
        #ADMIN SHOULD BE ABLE TO OVERRIDE IF DISPUTED
        #AFTER 3 Votes, VC SHOULD DISAPPEAR
        pass



    #sends embedded messages and removes player from queue
    if message.content.strip().lower() == '=l':
        len = bot.dq(message.author)
        embed = discord.Embed(description=f'{message.author.name} has left the queue.  **[{len}/4]**', color=0x0fbfcc) #out of 6 for 6mans
        #arbitrary return value so it doesn't clash with length of queue
        if len == 10:
            embed = discord.Embed(description="You can't leave a queue if you aren't in one ;)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send(embed=embed)
#=link, =mmr, and =edit mmr are all functions kieran will have to change


    if message.content.startswith('=link'):
        if word_list[1] in bot.rank.keys():
            x = bot.link_acct(word_list[1], message.author.name)
            if x == True:
                embed = discord.Embed(description="Account successfully linked :)", color=0x0fbfcc)
                await message.channel.send(embed=embed)
            else:
                embed = discord.Embed(description="Account could not be linked, either your account is already linked, or an error occured.", color=0x0fbfcc)
                await message.channel.send(embed=embed)
            #THEN IMMEDIATELY CREATE DATABASE USER WITH MMR AND RANK
    #ONLY FOR TESTING PURPOSES


    if message.content == "=mmr":
        mmr = bot.show_mmr(message.author.name)
        await message.channel.send(f'Your mmr is {mmr}')



    if message.content.startswith('=edit'):
        #SHOULD ONLY BE ACCESSIBLE BY ADMIN
        if len(word_list) == 3:
            mmr = bot.edit_mmr(word_list[1], word_list[2])
        else:
            embed = discord.Embed(description="This command was used incorrectly, should be used '=edit user mmr'", color=0x0fbfcc)
            await message.channel.send(embed=embed)



    if message.content == "=update":
        #ONLY ADMIN
        bot.update_rank(word_list[1], word_list[2])

    if message.content == "=profile":
        pass
        #DATABASEHIT
    if message.content == "=leaderboard":
        pass
        #DATABASEHIT
    if message.content == "=lobbyleaderboard":
        pass
        #DATABASEHIT

client.run("NzI0OTk2OTA2OTIwNzA2MDY4.XvahiQ.XxrWt3d-3yTOIfIqad9VyAyt6ek")
