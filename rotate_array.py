from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
answer = Solution()
print(answer.rotate([1,2,3,4,5,6,7], 3))
