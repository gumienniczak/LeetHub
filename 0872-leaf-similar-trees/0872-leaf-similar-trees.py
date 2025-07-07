# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        leafs_a = []
        leafs_b = []
        def dfs(root, leaf_list):
            if not root:
                return
            
            if not root.left and not root.right:
                leaf_list.append(root.val)

            left = dfs(root.left, leaf_list)
            right = dfs(root.right, leaf_list)

        dfs(root1, leafs_a)
        dfs(root2, leafs_b)
        return leafs_a == leafs_b

        