class Game:

    def __init__(self):
        self.queue = []
        self.game_id = 0
        
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

    def set_teams(self):

        self.queue = []
        self.game_id+=1
