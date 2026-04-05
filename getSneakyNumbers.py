from typing import List
from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        thislist = []
        p = Counter(nums)
        for i , j in p.items():
            if j > 1:
                thislist.append(i)
        return thislist


answer = Solution()
print(answer.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))
