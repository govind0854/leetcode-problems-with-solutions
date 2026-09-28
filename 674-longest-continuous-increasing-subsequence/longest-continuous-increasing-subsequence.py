class Solution(object):
    def findLengthOfLCIS(self, nums):
        c=1
        m=1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                c +=1
                m=max(m,c)
            else:
                c=1
                m=max(m,c)
        return m
        