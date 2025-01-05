class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)  # Difference array
        
        # Record shifts in the difference array
        for start, end, direction in shifts:
            shift = 1 if direction == 1 else -1
            delta[start] += shift
            if end + 1 < n:
                delta[end + 1] -= shift
        
        # Compute cumulative shifts
        cumulative_shift = 0
        result = []
        for i in range(n):
            cumulative_shift += delta[i]
            # Apply the cumulative shift to the current character
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)

        

        