class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for c in range(ord('a'), ord('z') + 1):
            c = chr(c)
            min_count = float('inf')
            for word in words:
                count = word.count(c)
                min_count = min(min_count, count)
                if min_count == 0:
                    break
            res.extend([c] * min_count)
        return res