from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        t = dict()
        for i in nums:
            if i not in t:
                t[i] = 1
            else:
                t[i] += 1
        for i, j in t.items():
            if j > 1:
                return True
        return False


answer = Solution()
print(answer.containsDuplicate([1,2,3,1]))