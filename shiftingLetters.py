from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ''
        j = 0
        for i in range(len(shifts) -1, -1, -1):
            res += chr((ord(s[i]) - ord('a') + j +shifts[i]) % 26 + ord('a'))
            j += shifts[i]
            print(j)
        return res[::-1]
    
reswer = Solution()
print(reswer.shiftingLetters("abc", [3,5,9]))