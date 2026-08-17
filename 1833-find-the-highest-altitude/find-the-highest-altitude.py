class Solution(object):
    def largestAltitude(self, gain):
        n=len(gain)
        prefix_sum=[0]
        rs=0
        for i in range(n):
            rs +=gain[i]
            prefix_sum.append(rs)
        return max(prefix_sum)


        
        