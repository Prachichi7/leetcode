from typing import List

class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = set()
            cnt_even = 0
            cnt_odd = 0

            for j in range(i, n):
                x = nums[j]
                if x not in seen:
                    seen.add(x)
                    if x % 2 == 0:
                        cnt_even += 1
                    else:
                        cnt_odd += 1

                if cnt_even == cnt_odd:
                    ans = max(ans, j - i + 1)

        return ans
        