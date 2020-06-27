
import random
import discord
import sqlite3
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
    def update(self, username, key, value):
        conn = sqlite3.connect('variables.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE users
        SET ?=?
        WHERE username=?''', (key, value, username))
    def read(self, username):
        conn = sqlite3.connect('variables.db')
        cursor = conn.cursor()
        username = f'\'{username}\''
        cursor.execute("SELECT mmr, wins, losses, draws, games, rank FROM users WHERE username=?;", (username,))
        print(cursor.fetchone())
        print(username)
        return cursor
    def create_user(self, username, mmr, rank):
        conn = sqlite3.connect('variables.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, mmr, wins, losses, draws, games, rank) VALUES (?, ?, 0, 0, 0, 0, ?)", (username, mmr, rank))
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
        x = self.read(user).fetchall()
        return x #self.player_dict[user]

    def edit_mmr(self, user, mmr):
        if mmr.isnumeric():
            self.player_dict[user] = mmr
        return

    def promote_rank(self, user):
        pass

    def win(self, user):
        pass

    def loss(self, user):
        pass

    def set_teams(self):

        self.queue = []
        self.game_id+=1

    def cancel_game(self):
        pass

    def link_acct(self, rank, user):
        self.player_dict[user] = self.rank[rank]
        if self.read(user).rowcount < 1:
            self.create_user(user, self.rank[rank], "Filler")


    def bad_words(self, message_list):
        #word filter
        no_no_words = ["nigger", 'nig', 'fag', 'faggot', 'gay', 'retarded', 'kys', 'retard']

        for word in no_no_words:
            for string in message_list:
                if string.strip().lower() == word:
                    return True
    def update_rank(self, user, rank):
        if self.read(user) is not None:
            self.update(user, 'mmr', rank)

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

    def create(self):
        conn = sqlite3.connect('variables.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            mmr INTEGER,
            wins INTEGER,
            losses INTEGER,
            draws INTEGER,
            games INTEGER,
            rank TEXT
            )
            ''')
