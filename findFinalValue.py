from typing import List
import sys
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == original:
                result = nums[i] * 2
                return self.findFinalValue(nums, result)
            i += 1
        return original

answer = Solution()
print(answer.findFinalValue([5,3,6,1,12], 3))