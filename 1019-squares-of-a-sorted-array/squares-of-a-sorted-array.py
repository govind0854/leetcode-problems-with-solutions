class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        ans = [0] * n

        left = 0
        right = n - 1
        k = n - 1

        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                ans[k] = nums[left] ** 2
                left += 1
            else:
                ans[k] = nums[right] ** 2
                right -= 1

            k -= 1

        return ans