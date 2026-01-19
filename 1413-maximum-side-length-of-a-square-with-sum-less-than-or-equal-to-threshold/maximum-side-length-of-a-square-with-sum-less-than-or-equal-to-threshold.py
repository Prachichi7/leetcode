class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def feasible(side_length: int) -> bool:
            for row in range(rows - side_length + 1):
                for col in range(cols - side_length + 1):
                    square_sum = (prefix_sum[row + side_length][col + side_length]
                                 - prefix_sum[row][col + side_length]
                                 - prefix_sum[row + side_length][col]
                                 + prefix_sum[row][col])
                    if square_sum <= threshold:
                        return True
            return False

        rows, cols = len(mat), len(mat[0])

        prefix_sum = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i, row in enumerate(mat, start=1):
            for j, value in enumerate(row, start=1):
                prefix_sum[i][j] = (prefix_sum[i - 1][j] + prefix_sum[i][j - 1]
                                   - prefix_sum[i - 1][j - 1] + value)

    
        left, right = 1, min(rows, cols) + 1
        first_true_index = min(rows, cols) + 1  

        while left <= right:
            mid = (left + right) // 2
            if not feasible(mid): 
                first_true_index = mid
                right = mid - 1  
            else:
                left = mid + 1

        return first_true_index - 1
        