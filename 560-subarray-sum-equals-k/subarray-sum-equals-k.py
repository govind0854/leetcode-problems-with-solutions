class Solution(object):
    def subarraySum(self, nums, k):
        # csum=0
        # left=0
        # subcnt=0
        # for right in range(len(nums)):
        #     csum += nums[right]
        #     while csum > k:
        #         csum -=nums[left]
        #         left +=1
        #     if csum==k:
        #         subcnt +=1
        # return subcnt
        seen={0:1}
        subcnt=0
        prefixsum=0
        for i in nums:
            #compute the prefix sum
            prefixsum +=i
            #calculate the required previous prefix we have to search
            req=prefixsum-k
            #check if req in seen prefixes(history of prefixes)

            if req in seen:
                #add the value to subcnt
                subcnt += seen[req]
            #crucial step:add the current prefixsum to history(seen)
            seen[prefixsum]=seen.get(prefixsum,0)+1
        return subcnt


        