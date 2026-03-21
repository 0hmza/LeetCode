from typing import List
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        thislist = []
        i = 0
        while i < len(nums):
            a = nums[i]
            j = i + 1
            while j < len(nums):
                if nums[j] == a:
                    thislist.append(nums[j])
                j += 1
            i += 1
        return thislist


answer = Solution()
print(answer.getSneakyNumbers([7,1,5,4,3,4,6,0,9,5,8,2]))