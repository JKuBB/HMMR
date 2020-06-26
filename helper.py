
import random
import discord
import csv

class Bot:

    def __init__(self):
        self.queue = []
        self.player_dict = {}
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

    def to_csv(self):

        with open('variables.csv', 'w', newline='') as csvfile:
            fieldnames = ["user", "mmr"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for key in self.player_dict.keys():
                writer.writerow(self.player_dict.get(key))


    def update_from_csv(self):
        with open('variables.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.player_dict[row['user']] = row

    def show_mmr(self, user):
        return self.player_dict[user]['mmr']

    def edit_mmr(self, user, mmr):
        if mmr.isnumeric():
            tempdict = {"user": user, "mmr": mmr}
            self.player_dict[user] = tempdict
            self.to_csv()
        return

    def promote_rank(self, user):
        self.to_csv()

    def win(self, user):
        self.to_csv()

    def loss(self, user):
        self.to_csv()

    def set_teams(self):

        self.queue = []
        self.game_id+=1

    def cancel_game(self):
        pass

    """
    The thought process behind this is to add a nested dictionary with a user's name as the key so that we can read and write rows of user data instead of 1 singular dictionary.
    should end up like this:
    {username: {"user": username, "mmr": mmr}}
    the get call for this would be player_dict[username]["mmr"] like a 2d array
    """
    def link_acct(self, platform, user):
        tempdict = {"user": user, "mmr": self.rank[platform]}
        self.player_dict[user] = tempdict
        self.to_csv()

    def bad_words(self, message_list):
        #word filter
        no_no_words = ["nigger", 'nig', 'fag', 'faggot', 'gay', 'retarded', 'kys', 'retard']

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
