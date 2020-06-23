class Bot:

    def __init__(self):
        self.queue = [None]*4
        self.q_spot = 0
        
    def q(self, username):
        self.queue[self.q_spot] = username
        self.q_spot += 1
        return (self.q_spot)

    def dq(self, username):
        if self.q_spot != 0:
            self.queue[self.q_spot] = None
            self.q_spot -= 1
            return (self.q_spot)
        return
