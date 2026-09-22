class Solution(object):
    def findDisappearedNumbers(self, nums):
        l=[]
        s=set()
        for i in range(len(nums)):
            s.add(nums[i])
        for i in range(1,len(nums)+1):
            if i not in s:
                l.append(i)
        return l
            
                
        