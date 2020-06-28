import sqlite3 as sqlite

class Database:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        conn = sqlite.connect(db_file_path)
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                UserId INTEGER PRIMARY KEY,
                Username TEXT,
                Mmr INTEGER,
                Wins INTEGER,
                Losses INTEGER,
                Draws INTEGER,
                Games INTEGER,
                Rank TEXT
            );
        ''')


        conn.commit()
        conn.close()

    def create_user(self, username, mmr, rank):
        if (self.get_user(username) is not None):
            raise Exception('A user with this username already exists')

        sql = '''
            INSERT INTO Users (
                Username,
                Mmr,
                Wins,
                Losses,
                Draws,
                Games,
                Rank
            )
            VALUES (
                ?,
                ?,
                0,
                0,
                0,
                0,
                ?
            )
        '''

        args = (username, mmr, rank)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def get_all_users(self):
        sql = "SELECT UserId, Username, Mmr, Wins, Losses, Draws, Games, Rank FROM Users"
        conn = sqlite.connect(self.db_file_path)

        cursor = conn.cursor()
        cursor.execute(sql)

        users = cursor.fetchall()

        conn.close()

        return users

    def get_user(self, username):
        sql = "SELECT UserId, Username, Mmr, Wins, Losses, Draws, Games, Rank FROM Users WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        cursor = conn.cursor()
        cursor.execute(sql, args)

        results = cursor.fetchall()
        user = None

        if (len(results) > 0):
            user = results[0]

        conn.close()

        return user

    def increment_user_win(self, username):
        sql = "UPDATE Users SET Wins = Wins + 1 WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def increment_user_loss(self, username):
        sql = "UPDATE Users SET Losses = Losses + 1 WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def increment_user_draw(self, username):
        sql = "UPDATE Users SET Draws = Draws + 1 WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def increment_user_game(self, username):
        sql = "UPDATE Users SET Games = Games + 1 WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def increment_user_mmr(self, username, mmr):
        sql = "UPDATE Users SET Mmr = Mmr + ? WHERE Username = ?"
        args = (mmr, username)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def set_user_mmr(self, username, mmr):
        sql = "UPDATE Users SET Mmr = ? WHERE Username = ?"
        args = (mmr, username)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()
    def set_user_rank(self, username, rank):
        sql = "UPDATE Users SET Rank = ? WHERE Username = ?"
        args = (rank, username)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()

    def delete_user(self, username):
        sql = "DELETE FROM Users WHERE Username = ?"
        args = (username,)

        conn = sqlite.connect(self.db_file_path)

        conn.execute(sql, args)

        conn.commit()

        conn.close()
