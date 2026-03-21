from typing import List
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        i = 0
        start = -1
        while i < len(nums):
            if nums[i] == 1:
                if start != -1:  ### je neux pas calculer espcae de premier avec rien
                    space = i - start - 1
                    if space < k:
                        return False
                start = i
            i += 1
        return True


answer = Solution()

print(answer.kLengthApart([0,0,0], 2))
print(answer.kLengthApart([1,0,0,0,1,0,0,1], 2))
print(answer.kLengthApart([1,0,0,1,0,1], 2))
print(answer.kLengthApart([0,1,1,0,1], 4))
print(answer.kLengthApart([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], 32))
print(answer.kLengthApart([0,1,0,1], 1))