class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        num_dict = defaultdict(int)
        for i in nums:
            if num_dict[i] == 1:
                num_dict.pop(i)
            else:
                num_dict[i] += 1
        return num_dict.keys()