class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        vowels = 'aeiouAEIOU'
        sList = list(s)
        while(l < r):
            if sList[l] not in vowels:
                l += 1
                continue
            if sList[r] not in vowels:
                r -= 1
                continue
            sList[l], sList[r] = sList[r], sList[l]
            l += 1
            r -= 1
        return "".join(sList)