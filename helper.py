from discord.utils import get
import random
import discord
import sqlite3
import time
import threading
from database import Database

class Bot:

    def __init__(self):
        self.db = Database("bot_data.db")
        self.rank = {
        "gold": 650,
        "platinum": 840,
        "diamond": 980,
        "champion": 1300,
        "grandchampion": 1500
        }
        self.rank_bounds = {
        "B": 980,
        "A": 1380
        }

    def show_mmr(self, user):
        mmr = self.db.get_user(user)
        return mmr[2]

    def get_profile(self, user):
        pass

#LOOK AT THIS FUNCTION BEFORE DONE
    def edit_mmr(self, user, mmr):
        if mmr.isnumeric():
            self.db.set_user_mmr(user, mmr)

    def promote_rank(self, user):
        pass

    async def link_acct(self, RLrank, message):
        user = message.author.id

        if (self.db.get_user(user) is None):
            rank = ""
            if(self.rank[RLrank] > self.rank_bounds["B"]):
                rank = "B"
                if(self.rank[RLrank] > self.rank_bounds["A"]):
                    rank = "A"
            else:
                rank = "C"
            self.db.create_user(user, self.rank[RLrank], rank)
            #call db set rank and pass in mmr and assign in the function to the db based on mmr
            x = rank
        else:
            x = False
        await self.handle_link(x, message)


    def bad_words(self, message_list):
        #word filter
        no_no_words = ["nigger", 'nig', 'fag', 'faggot', 'gay', 'retarded', 'kys', 'retard', "!david"]

        for word in no_no_words:
            for string in message_list:
                if string.strip().lower() == word:
                    return True

    def update_rank(self, user, rank):
        if self.db.get_user(user) is not None:
            self.db.set_user_rank(user, rank)

    def nine_nine(self):
        #returns a random B99 quote
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!', "Nine Nine!",
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        return random.choice(brooklyn_99_quotes)
    #returns the role given by 'rank x'
    #CAUTION DEADLOCK, MAY BE BENEFICIAL TO LOCK THREAD
    def get_role(self, message, x):
        rankname = f'rank {x}'
        guild = message.guild
        return get(guild.roles, name=f'rank {x}')

    #sets rank name, creates a category, text channel, and assigns role to message author
    #CAUTION DEADLOCK, MAY BE BENEFICIAL TO LOCK THREAD
    async def create_new_role(self, x, guild):
        rankname = f'rank {x}'
        category = await guild.create_category(rankname)
        #WE HAVE TO ONLY MAKE THIS VISIBLE TO PEOPLE IN RANK
        await guild.create_text_channel(rankname, category=category)
        await guild.create_role(name=rankname)
        role = get(guild.roles, name=rankname)
        await message.author.add_roles(role)

    #checks message to get the role of the command
    #if the role does not exist, it creates the role
    #if the role does exist, it adds the role to the author.
    #CAUTION DEADLOCK, MAY BE BENEFICIAL TO LOCK THREAD
    async def add_user_role(self, message, x):
        role = self.get_role(message, x)
        if role != None:
            await message.author.add_roles(role)
        else:
            await self.create_new_role(x, message.guild)

    async def handle_link (self, x, message):
        if x != False:
            #sends message off to helper functions to do magic with it
            await self.add_user_role(message, x)
            embed = discord.Embed(description="Account successfully linked :)", color=0x0fbfcc)
            await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(description='Account could not be linked, either your account is already linked, or an error occured.', color=0x0fbfcc)
            await message.channel.send(embed=embed)
