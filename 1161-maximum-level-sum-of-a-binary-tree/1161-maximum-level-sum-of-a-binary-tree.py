from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        i = 0
        current_level = deque([root])
        biggest_sum = float('-inf')
        sums = []
        while current_level:
            curr_len = len(current_level)
            curr_sum = 0
            i += 1
            for _ in range(curr_len):
                node = current_level.popleft()
                curr_sum += node.val
                if node.left:
                    current_level.append(node.left)
                if node.right:
                    current_level.append(node.right)
            
            sums.append((i, curr_sum))

        return max(sums, key = lambda x: x[-1])[0]
        