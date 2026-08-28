class Solution(object):
    def checkSubarraySum(self, nums, k):
        seen={0:-1}
        csum=0
        for i in range(len(nums)):
            csum +=nums[i]
            rem=csum%k
            if rem in seen:
                if i-seen[rem] >=2:
                    return True
            else:
                    seen[rem]=i
        return False


        