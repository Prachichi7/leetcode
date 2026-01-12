class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        total_time= 0
        for i in range(len(points) - 1):
            current_point = points[i]
            next_point = points[i + 1]
          
            x_distance = abs(current_point[0] - next_point[0])
            y_distance = abs(current_point[1] - next_point[1])
          
            time_between_points = max(x_distance, y_distance)
          
            total_time += time_between_points
      
        return total_time
        