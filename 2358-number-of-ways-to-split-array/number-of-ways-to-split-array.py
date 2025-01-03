class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res = 0
        left_sum = 0
        right_sum = sum(nums)  # Total sum

        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum -= nums[i]
            if left_sum >= right_sum:
                res += 1

        return res