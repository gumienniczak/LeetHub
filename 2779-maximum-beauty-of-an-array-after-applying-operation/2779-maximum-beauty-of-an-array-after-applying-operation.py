class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
    
        events = defaultdict(int)
        for num in nums:
            events[num - k] += 1
            events[num + k + 1] -= 1
    
        max_beauty = 0
        current_overlap = 0
        for key in sorted(events):
            current_overlap += events[key]
            max_beauty = max(max_beauty, current_overlap)
    
        return max_beauty