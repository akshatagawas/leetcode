class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def cBalls(d):
            numBalls, cur = 1, position[0]
            for i in range(1, n):
                if position[i] - cur >= d:
                    numBalls += 1
                    cur = position[i]
            return numBalls
        
        left, right = 1, position[-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if cBalls(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right