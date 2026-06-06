class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        
        # Initialize left sum as 0 (no elements to the left initially)
        left_sum = 0
        # Initialize right sum as the total sum of all elements
        right_sum = sum(nums)
      
        # List to store the absolute differences
        result = []
      
        # Iterate through each element in the array
        for num in nums:
            # Exclude current element from right sum (elements after current)
            right_sum -= num
          
            result.append(abs(left_sum - right_sum))
          
            left_sum += num
      
        return result