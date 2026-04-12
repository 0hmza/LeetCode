from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = len(nums1) - 1
        while i >= m:
            nums1.pop()
            i -= 1
        j = len(nums2) - 1
        while j >= n:
            nums2.pop()
            j -= 1
        for k in nums2:
            nums1.append(k)
        nums1.sort()
        print(nums1)


answer = Solution()
answer.merge([1,2,3,0,0,0], 3,[2,5,6], 1 )