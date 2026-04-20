from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = dict()
        i = 0
        while i < len(nums):
            k = target - nums[i]
            if k in p:
                return [i, k]
            p[k] = i
            print(p[k])
            i += 1




answer = Solution()
print(answer.twoSum([2,7,11, 15], 9))