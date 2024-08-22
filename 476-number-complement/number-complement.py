class Solution:
    def findComplement(self, num: int) -> int:
        binNum = bin(num).replace("0b", "")
        res = ""
        for i in binNum:
            if i == '1':
                res += '0'
            else:
                res += '1'
        return int(res, 2)