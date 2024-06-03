class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        res = 0
        while(i < len(t) and j < len(s)):
            if s[j] == t[i]:
                j += 1
                i += 1
            else:
                j += 1
        if i != len(t):
            res = len(t[i:])
        return(res)