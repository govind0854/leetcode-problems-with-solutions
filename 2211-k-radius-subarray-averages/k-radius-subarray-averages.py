class Solution(object):
    def getAverages(self, nums, k):
        r=[-1]*len(nums)
        left=0
        centre=k
        window_size=2*k+1
        s=0
        if window_size > len(nums):
            return r
        for i in range(window_size):
            s +=nums[i]
        a=s/window_size
        r[centre]=a
        for i in range(window_size,len(nums)):
            s -= nums[left]
            s += nums[i]
            left += 1
            g= s/window_size
            centre +=1
            r[centre]=g
        return r
        
        
        