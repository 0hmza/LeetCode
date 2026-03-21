class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thislist = []
        j = 0
        i = 0
        for i in range(0, len(nums) -1):
            a = nums[i]
            j = j + i
            for j in range(i, len(nums)):
                b = nums[j]
                if a + b == target and i != j:
                    thislist.append(i)
                    thislist.append(j)
                    return thislist