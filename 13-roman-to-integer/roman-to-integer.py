class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_value = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
      
        from itertools import pairwise
      
        result = sum(
            (-1 if roman_to_value[current] < roman_to_value[next_char] else 1) * roman_to_value[current] 
            for current, next_char in pairwise(s)
        )
      
        result += roman_to_value[s[-1]]
      
        return result  