import discord
from discord.utils import get
import random
from game import Game
from helper import Bot
import threading
#upon linking, rank channels need to be accessible only by those in said ranks
#updates and database hits
#ADD ERROR MESSAGES FOR COMMANDS AND A PROPER COMMAND LIST
client = discord.Client()
bot = Bot()
game = Game()
#gets info from last time bot was online
#add constants for colors



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
        embed = game.q(message.author)
        await message.channel.send(embed=embed)
        queue_message = game.check_q_full()
        if queue_message:
            await message.channel.send(queue_message)
            teams = game.set_teams()
            #create voice channels, and captain selection for teams
    if message.content.strip().lower() == '=l':
        embed = game.dq(message.author)
        await message.channel.send(embed=embed)

    if message.content.strip().lower().startswith("=vote"):
        #ADMIN SHOULD BE ABLE TO OVERRIDE IF DISPUTED
        #AFTER 3 Votes, VC SHOULD DISAPPEAR, shold store who needs to be voting so randos cant
        pass

    if message.content.startswith('=link'):
        if word_list[1] in bot.rank.keys():
            await bot.link_acct(word_list[1], message)

    if message.content == "=mmr":
        mmr = bot.show_mmr(message.author.id)
        await message.channel.send(f'Your mmr is {mmr}')

    if message.content.startswith('=edit'):
        #SHOULD ONLY BE ACCESSIBLE BY ADMIN
        role = get(message.guild.roles, name='Admin')
        if(role in message.author.roles):
            if len(word_list) == 3:
                for member in message.mentions:
                    mmr = bot.edit_mmr(member.id, word_list[2])
            else:
                embed = discord.Embed(description="This command was used incorrectly, should be used '=edit user mmr'", color=0x0fbfcc)
                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(description="You do not have permission to use this command.", color=0x0fbfcc)
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

client.run("")
