
import random
import discord

class Bot:

    def __init__(self):
        self.queue = []

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


    def edit_mmr(self, user):
        pass

    def promote_rank(self, user):
        pass

    def win(self, user):
        pass

    def loss(self, user):
        pass

    def set_teams(self):
        pass

    def cancel_game(self):
        pass

    def link_acct(self, platform, user):
        pass

    def bad_words(self, message_list):
        #word filter
        no_no_words = ["nigger", 'nig', 'smurf', 'fag', 'faggot', 'gay', 'retarded']

        for word in no_no_words:
            for string in message_list:
                if string.strip().lower() == word:
                    return True

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
