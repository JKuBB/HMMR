import discord

class Game:
    #NEED TO ADD GAME AS AN OBJECT THAT NEEDS TO BE CREATED PER LOBBY IF ONE DOESN'T EXIST

    def __init__(self):
        self.queue = []
        self.game_id = 0
        self.BLUE = 0x0fbfcc

    def q(self, user):
        if user not in self.queue:
            self.queue.append(user)
            print(self.queue)
            bool = True
        else:
            bool = False

        embed = self.pick_q_message(user.name, bool)
        return embed

    def dq(self, user):
        if user in self.queue:
            self.queue.remove(user)
            bool = True
        else:
            bool = False
        embed = self.pick_dq_message(user.name, bool)
        return embed

    def q_timeout(self, user):
        if len(self.queue) != 0:
            if user in self.queue:
                self.queue.remove(user)
                return True

    def pick_q_message(self, user, bool):
        if bool == False:
            embed = discord.Embed(description="You can't join a queue if you're already in one ;)", color=self.BLUE)
        else:
            if not self.check_q_full():
                embed = discord.Embed(description=f'{user} has entered the queue.  **[{len(self.queue)}/4]**', color=self.BLUE)
            else:
                embed = discord.Embed(description="Queue is full. Picking teams...", color=self.BLUE)
        return embed

    def pick_dq_message(self, user, bool):
        if bool == True:
            embed = discord.Embed(description=f'{user} has left the queue.  **[{len(self.queue)}/4]**', color=self.BLUE) #out of 6 for 6mans
        else:
            embed = discord.Embed(description="You can't leave a queue if you aren't in one ;)", color=self.BLUE)

        return embed

    def check_q_full(self):
        if len(self.queue) == 2:
            embed=''
            for user in range(len(self.queue)):
                embed +='  <@' + str(self.queue[user].id) + '>'

            return embed
        else:
            return None

    def set_teams(self):

        self.queue = []
        self.game_id+=1

    def win(self, user):
        pass

    def loss(self, user):

        pass
