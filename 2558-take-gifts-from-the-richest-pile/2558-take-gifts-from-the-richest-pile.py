class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            index, value = max(enumerate(gifts), key = lambda x: x[1])
            gifts[index] = int(value ** (1 / 2))
        return sum(gifts)