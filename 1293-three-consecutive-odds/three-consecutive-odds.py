class Solution(object):
    def threeConsecutiveOdds(self, arr):
        m=0
        c=0
        for i in arr:
            if i%2!=0:
                c +=1
                m=max(m,c)
            else:
                c=0
        if m >= 3:
            return True
        else:
            return False
        
        