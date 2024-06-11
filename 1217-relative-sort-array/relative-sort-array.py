class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        for n in arr2:
            if n not in arr1:
                res.append(n)
            else:
                cnt = arr1.count(n)
                for i in range(cnt):
                    res.append(n)
                    arr1.remove(n)
        if arr1:
            res += sorted(arr1)
        return(res)
