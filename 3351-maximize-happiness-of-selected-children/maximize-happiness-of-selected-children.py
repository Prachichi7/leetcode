class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total_happiness = 0
      
        for turn_index, happiness_value in enumerate(happiness[:k]):
            adjusted_happiness = happiness_value - turn_index
            total_happiness += max(adjusted_happiness, 0)
      
        return total_happiness
        