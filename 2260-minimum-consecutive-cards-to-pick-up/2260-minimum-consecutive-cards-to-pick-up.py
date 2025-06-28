class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        ans = -1
        seen = set()
        for right in range(len(cards)):
            if cards[right] in seen:
                if ans != -1:
                    ans = min(ans, right + 1)
                else:
                    ans = right + 1
            
            seen.add(cards[right])
        return ans