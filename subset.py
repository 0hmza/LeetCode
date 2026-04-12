from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            ret += [r + [n] for r in ret]

        return ret


answer = Solution()
print(answer.subsets([1,2,3]))


def mySqrt(x: int) -> int:
    i = 1
    while i <= x:
        if i * i == x:
            return int(i)
        i += 1
    return 1
print(mySqrt(8))