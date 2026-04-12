from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return  sorted([c ** 2 for c in nums])
        


print(2**2)
answer = Solution()
print(answer.sortedSquares([-4,-1,0,3,10]))