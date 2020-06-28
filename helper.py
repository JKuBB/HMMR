
import random
import discord
import sqlite3
import time
import threading
from database import Database

class Bot:

    def __init__(self):
        self.db = Database("bot_data.db")
        self.queue = []
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
        self.game_id = 1
        self.WAIT_SECONDS = 3

    def q(self, user):
        if user not in self.queue:
            self.queue.append(user)
            length = len(self.queue)
            return length
        else:
            return 10

    def dq(self, user):
        if user in self.queue:
            self.queue.remove(user)
            return len(self.queue)
        else:
            return 10

    def q_timeout(self,user):
        if len(self.queue) != 0:
            if user in self.queue:
                self.queue.remove(user)
                return True

    def show_mmr(self, user):
        mmr = self.db.get_user(user)
        return mmr[2]

    def get_profile(self, user):
        pass

#LOOK AT THIS FUNCTION BEFORE DONE
    def edit_mmr(self, user, mmr):
        if mmr.isnumeric():
            pass


    def promote_rank(self, user):
        pass

    def win(self, user):
        pass

    def loss(self, user):
        pass

    def set_teams(self):

        self.queue = []
        self.game_id+=1

    def link_acct(self, RLrank, user):
        print(user)

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
            return rank
        else:
            return False


    def bad_words(self, message_list):
        #word filter
        no_no_words = ["nigger", 'nig', 'fag', 'faggot', 'gay', 'retarded', 'kys', 'retard']

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
