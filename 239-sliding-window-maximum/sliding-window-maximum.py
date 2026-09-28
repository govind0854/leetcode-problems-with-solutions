class Solution(object):
    def maxSlidingWindow(self, nums, k):
        #sliding window + monotonic deque solution
        q=deque()
        ans=[]
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:#here we are using nums[q[-1]], beacause we are sorting indices in queue not values
                q.pop()
            q.append(i)
            #queue front will have max element
        ans.append(nums[q[0]])
        for i in range(k,len(nums)):
            if q[0]==i-k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:# here we are using nums[q[-1]], beacuse we are sorting indices in queue not values
                q.pop()
            q.append(i)
            ans.append(nums[q[0]])
        return ans

        