# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        """
        current_level = deque([root])
        ans = []
        while current_level:
            curr_vals = []
            n = len(current_level)
            for _ in range(n):
                node = current_level.popleft()
                curr_vals.append(node.val)
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
                
            ans.append(sum(curr_vals) / float(n))

        return ans

        