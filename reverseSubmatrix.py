from typing import List
class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2): 
            for j in range(k):
                temp = grid[x + i][y + j] 
                grid[x + i][y + j] = grid[x + k - 1 - i][y + j]
                grid[x + k - 1 - i][y + j] = temp
                
        return grid

answer = Solution()
print(answer.reverseSubmatrix([[3,4,2,3],[2,3,4,2]], 0, 2, 2))
