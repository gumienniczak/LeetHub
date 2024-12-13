import heapq
class Solution:
    def findScore(self, nums: List[int]) -> int:
        score = 0
        n = len(nums)
        array_marked = [0] * n  # Keeps track of marked indices

        # Create a min-heap with (value, index) pairs
        min_heap = [(value, i) for i, value in enumerate(nums)]
        heapq.heapify(min_heap)

        while min_heap:
            value, index = heapq.heappop(min_heap)

            # Skip if the index is already marked
            if array_marked[index] == 1:
                continue

            # Add the value to the score and mark the index
            score += value
            array_marked[index] = 1

            # Mark neighbors
            if index - 1 >= 0:
                array_marked[index - 1] = 1
            if index + 1 < n:
                array_marked[index + 1] = 1

        return score