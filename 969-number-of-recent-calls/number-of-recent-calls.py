class RecentCounter(object):

    def __init__(self):
        self.d=deque()
        

    def ping(self, t):
        while self. d and self.d[0] < t- 3000:
            self.d.popleft()
        self.d.append(t)
        return len(self.d)

        
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)