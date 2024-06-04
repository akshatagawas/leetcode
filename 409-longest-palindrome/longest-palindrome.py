class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        t = set()
        for i in s:
            if i in t:
                t.remove(i)
                res += 2
            else:
                t.add(i)
        if t:
            res += 1
        return res