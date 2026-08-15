class Solution(object):
    def findMaxAverage(self, nums, k):
        window_sum = 0
        left = 0
        for i in range(k):
            window_sum += nums[i]
        max_avg = float(window_sum) / k
        for i in range(k, len(nums)):
            window_sum -= nums[left]
            window_sum += nums[i]
            left += 1
            current_avg = float(window_sum) / k
            max_avg = max(max_avg, current_avg)
        return max_avg