
import random
import discord
import Linked_List

class Bot:

    def __init__(self):
        self.queue = [None]*4

    def q(self, username):
        pass

    def dq(self, username):
        pass

    def edit_mmr(self, username):
        pass

    def promote_rank(self, username):
        pass

    def win(self, username):
        pass

    def loss(self, username):
        pass

    def set_teams(self, username):
        pass

    def cancel_game(self):
        pass

    def link_acct(self, platform, username):
        pass

    def bad_words(self, message):
        #word filter
        no_no_words = ["nigger", 'nig', 'smurf', 'fag', 'faggot', 'gay', 'retarded']

        for word in no_no_words:
            if message.strip().lower() == word:
                return True

    def nine_nine(self):
        #returns a random B99 quote
        brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
        ]

        return random.choice(brooklyn_99_quotes)
