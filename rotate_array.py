from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        return nums[::-k]

answer = Solution()
print(answer.rotate([1,2,3,4,5,6,7], 3))
