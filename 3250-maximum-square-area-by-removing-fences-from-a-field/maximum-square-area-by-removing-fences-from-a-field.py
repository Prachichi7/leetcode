class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        def get_all_distances(fence_positions: List[int], field_size: int) -> Set[int]:
            all_positions = fence_positions + [1, field_size]
            all_positions.sort()
          
            distances = set()
            for i in range(len(all_positions)):
                for j in range(i + 1, len(all_positions)):
                    distance = all_positions[j] - all_positions[i]
                    distances.add(distance)
          
            return distances
      
        MOD = 10**9 + 7
    
        horizontal_distances = get_all_distances(hFences, m)
      
        vertical_distances = get_all_distances(vFences, n)
    
        common_distances = horizontal_distances & vertical_distances
      
        max_side_length = max(common_distances, default=0)
   
        if max_side_length > 0:
            area = (max_side_length ** 2) % MOD
            return area
        else:
            return -1
        