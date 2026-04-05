from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        thislist = []
        i = 0
        while i < len(nums):
            if nums[i] == target:
                thislist.append(i)
            i += 1
        if len(thislist) == 0:
            return [-1, -1]
        if len(thislist) == 1:
            a = thislist[0]
            return [a,a]
        if len(thislist) > 1:
            return [thislist[0], thislist[len(thislist) -1]]



answer = Solution()
print(answer.searchRange([11,3, 3, 23,3,4, 5,6 ,7 ,3], 3))