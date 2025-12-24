class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples = sum(apple)
        for index, box_capacity in enumerate(capacity, 1):
            total_apples -= box_capacity
            if total_apples <= 0:
                return index
        