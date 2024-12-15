import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # Initialize a max-heap with negative ratios
        # Calculate the marginal gain and use a max-heap
        heap = [(-(self.gain(p, t)), p, t) for p, t in classes]
        heapq.heapify(heap)  # Max-heap using negative gain

        # Distribute the extra students
        while extraStudents > 0:
            neg_gain, p, t = heapq.heappop(heap)  # Get the class with the highest marginal gain
            p += 1
            t += 1
            extraStudents -= 1
            heapq.heappush(heap, (-(self.gain(p, t)), p, t))  # Recalculate and push back

        # Calculate the final average ratio
        total_average = sum(p / t for _, p, t in heap) / len(classes)
        return total_average
    
    def gain(self, p: int, t: int) -> float:
        """Calculate the marginal gain of adding one student."""
        return (p + 1) / (t + 1) - p / t