import re

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        longest_length = -1
    
        # Generate all substrings of single repeated characters
        for length in range(1, n + 1):  # Length of substrings to check
            substring_counts = Counter(s[i:i+length] for i in range(n - length + 1))
        
            for substring, count in substring_counts.items():
                if len(set(substring)) == 1 and count >= 3:  # Check if special and occurs at least 3 times
                    longest_length = max(longest_length, len(substring))
    
        return longest_length