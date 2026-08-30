class Solution(object):
    def maximumWealth(self, accounts):
        m=0
        s=0
        for i in accounts:
            s=sum(i)
            if s > m:
                m=s
        return m

        

        
        