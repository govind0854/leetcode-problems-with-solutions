class Solution(object):
    def predictPartyVictory(self, senate):
        r=deque()
        d=deque()
        n=len(senate)
        for i in range(n):
            if senate[i]=="R":
                r.append(i)
            else:
                d.append(i)
        #invalidation during voting
        while r and d:
            if r[0] < d[0]:
                d.popleft()
                r.append(r.popleft()+n)
            else:
                r.popleft()
                d.append(d.popleft()+n)
        return 'Dire' if d else 'Radiant'

        
        

          
        