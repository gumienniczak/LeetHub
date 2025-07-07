# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root_a, root_b):
            if not root_a and not root_b:
                return True
            if root_a and not root_b:
                return False
            if not root_a and root_b:
                return False
            
            if root_a.val != root_b.val:
                return False

            left = dfs(root_a.left, root_b.left)
            right = dfs(root_a.right, root_b.right)

            return left and right
        return dfs(p, q)