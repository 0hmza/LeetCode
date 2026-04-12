from typing import List
class Solution:
    def search(self, nums, target):
        i = 0
        while i < len(nums):
            if nums[i] == target:
                return i
            i +=1
        return -1


answer = Solution()
print(answer.search([4,5,6,7,0,1,2], 3))