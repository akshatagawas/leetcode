class Solution:
    def maxScore(self, s: str) -> int:
        max_sum = float("-inf")
        for i in range(1,len(s)):
            left = s[:i].count("0")
            right = s[i:].count("1")
            max_sum = max(max_sum, left+right)
        return max_sum