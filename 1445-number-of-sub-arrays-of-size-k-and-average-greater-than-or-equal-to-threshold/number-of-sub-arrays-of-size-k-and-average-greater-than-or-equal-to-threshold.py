class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        left=0
        c=0
        window_sum=0
        for i in range(k):
            window_sum +=arr[i]
        if window_sum >= k*threshold:
            c +=1
        for i in range(k,len(arr)):
            window_sum -=arr[left] 
            window_sum +=arr[i]
            if window_sum >=k*threshold:
                c +=1
            left +=1
        return c


            
        
        
        
        