class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for number in nums:
            digits_stack = []
          
            while number > 0:
                digit = number % 10
                digits_stack.append(digit)
                number //= 10 
          
            result.extend(digits_stack[::-1])
      
        return result
        