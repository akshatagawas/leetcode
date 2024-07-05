class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCan = max(candies)
        res = []
        for i in candies:
            if i + extraCandies >= maxCan:
                res.append(True)
            else:
                res.append(False)
        return res