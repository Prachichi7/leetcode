class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba_pattern_count = 6  
        abc_pattern_count = 6  
      
        for column_index in range(n - 1):
            next_aba_count = (3 * aba_pattern_count + 2 * abc_pattern_count) % MOD
            next_abc_count = (2 * aba_pattern_count + 2 * abc_pattern_count) % MOD
          
            aba_pattern_count = next_aba_count
            abc_pattern_count = next_abc_count

        return (aba_pattern_count + abc_pattern_count) % MOD
        