class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        seen = set()
        cur = (0, 0)
        seen.add(cur)
        x = 0
        y = 0
        for step in path:
            if step == 'N':
                y += 1
            elif step == 'E':
                x += 1
            elif step == 'S':
                y -= 1
            elif step == 'W':
                x -= 1

            if (x, y) in seen:
                return True
            
            seen.add((x, y))

        return False
        