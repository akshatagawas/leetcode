class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed.append(0)
        for i in range(len(flowerbed) - 1):
            if flowerbed[i] == 0 and n:
                if(flowerbed[i + 1] == 0 and i == 0) or (i == len(flowerbed) - 1 and flowerbed[i - 1] == 0):
                    n -= 1
                    flowerbed[i] = 1
                elif(flowerbed[i -1] == 0 and flowerbed[i + 1] == 0):
                    n -= 1
                    flowerbed[i] = 1
            else:
                continue
        if n:
            return False
        else:
            return True