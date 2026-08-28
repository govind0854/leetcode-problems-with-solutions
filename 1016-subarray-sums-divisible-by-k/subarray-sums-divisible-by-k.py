class Solution(object):
    def subarraysDivByK(self, nums, k):
        seen={0:1}
        subcnt=0
        csum=0
        for i in range(len(nums)):
            csum += nums[i]
            req=csum%k

            if req in seen:
                subcnt +=seen[req]
            seen[req]=seen.get(req,0)+1
        return subcnt
        
        
        