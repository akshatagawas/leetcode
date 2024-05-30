class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        N = len(arr)
        res = 0
        prefix = 0
        prev_XOR = defaultdict(int)
        prev_XOR_idx = defaultdict(int)
        prev_XOR[0] = 1

        for i in range(N):
            prefix ^= arr[i]
            if prev_XOR[prefix]:
                res += i * prev_XOR[prefix] - prev_XOR_idx[prefix]

            prev_XOR[prefix] += 1
            prev_XOR_idx[prefix] += i + 1
        return res