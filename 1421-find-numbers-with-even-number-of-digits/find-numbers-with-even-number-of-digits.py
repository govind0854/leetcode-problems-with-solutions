class Solution(object):
    def findNumbers(self, nums):
        c=0
        for i in nums:
            v=str(i)
            value=len(v)
            if value%2==0:
                c +=1
        return c
        
        