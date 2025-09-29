class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        counter = 0
        for stone in stones:
            if stone in jewels:
                counter += 1
        
        return counter