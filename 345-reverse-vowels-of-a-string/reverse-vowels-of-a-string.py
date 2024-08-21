class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        strList = list(s)
        i, j = 0, len(strList)-1 
        while(i < j):
            while strList[i] not in vowels and i < len(strList)-1:
                i += 1
                print(i, j)
            while strList[j] not in vowels and j > -1:
                j -= 1
            if i < j:
                strList[i], strList[j] = strList[j], strList[i]
                i += 1
                j -= 1
        return "".join(strList)
            
