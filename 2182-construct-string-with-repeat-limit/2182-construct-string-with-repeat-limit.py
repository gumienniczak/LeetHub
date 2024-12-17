from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        # Count frequency of each character
        freq = Counter(s)
        
        # Use a max-heap (negate ord values to sort in descending order)
        max_heap = [(-ord(char), char) for char in freq]
        heapq.heapify(max_heap)
        
        result = []
        while max_heap:
            # Get the lexicographically largest character available
            neg_ord, char = heapq.heappop(max_heap)
            
            if result and result[-1] == char and len(result) >= repeatLimit:
                # If the current character has hit its repeat limit
                if not max_heap:
                    # If there's no other character to use, stop
                    break
                
                # Get the next largest character
                next_neg_ord, next_char = heapq.heappop(max_heap)
                result.append(next_char)
                
                # Decrement the frequency of the second largest character
                freq[next_char] -= 1
                if freq[next_char] > 0:
                    heapq.heappush(max_heap, (next_neg_ord, next_char))
                
                # Push the original character back into the heap
                heapq.heappush(max_heap, (neg_ord, char))
            else:
                # Add the character up to the repeat limit
                max_add = min(repeatLimit, freq[char])
                result.extend([char] * max_add)
                
                # Decrement frequency
                freq[char] -= max_add
                if freq[char] > 0:
                    heapq.heappush(max_heap, (neg_ord, char))
        
        return "".join(result)
