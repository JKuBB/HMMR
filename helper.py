
import random
import discord
import sqlite3
from database import Database

class Bot:

    def __init__(self):
        self.db = Database()
        self.queue = []
        self.rank = {
        "gold": 650,
        "platinum": 840,
        "diamond": 980,
        "champion": 1300,
        "grandchampion": 1500
        }
        self.game_id = 1

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

    def show_mmr(self, user):
        x = self.db.get_user(user)
        return x["Mmr"]

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

    def link_acct(self, rank, user):
        print(user)
        if (self.db.get_user(user) is None):
            self.db.create_user(user, self.rank[rank], "Filler")
            return True
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
