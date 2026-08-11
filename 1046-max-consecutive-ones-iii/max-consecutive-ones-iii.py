class Solution(object):
    def longestOnes(self, nums, k):
        # d={}
        # for i in nums:
        #     if i in d:
        #         d[i]+=1
        # print(d[i])
        z=0
        m=0
        left=0
        for i in range(len(nums)):
            if nums[i]==0:
                z +=1
            while z > k:
                if nums[left]==0:
                    z -=1
                left+=1
            m=max(m,i-left+1)
        return m
        



       
        