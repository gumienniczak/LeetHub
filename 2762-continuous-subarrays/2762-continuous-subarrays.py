from sortedcontainers import SortedList

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        result = 0
        window = SortedList()  # To maintain a sorted window
    
        for right in range(n):
            window.add(nums[right])  # Add the new element to the window
        
            # Shrink the window if the condition is violated
            while window[-1] - window[0] > 2:
                window.remove(nums[left])
                left += 1
        
            # Count all valid subarrays ending at 'right'
            result += right - left + 1
    
        return result