class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        total_count = 0

        for row in range(rows):
            left, right = 0, cols - 1
            first_true_index = -1

            while left <= right:
                mid = (left + right) // 2
                if grid[row][mid] < 0:
                    first_true_index = mid
                    right = mid - 1 
                else:
                    left = mid + 1
            
            if first_true_index != -1:
                total_count += cols - first_true_index

        return total_count
        