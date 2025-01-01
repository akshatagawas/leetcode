class Solution:
    def maxScore(self, s: str) -> int:
        max_sum = float("-inf")
        for i in range(1,len(s)):
            max_sum = max(max_sum, s[:i].count("0")+s[i:].count("1"))
        return max_sum