# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        queue = deque([root])
        level = 0

        result = []

        while queue:
            size = len(queue)
            current_level_values = []

            for _ in range(size):
                node = queue.popleft()
                current_level_values.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
  
            result.append(max(current_level_values))  

            level += 1
        
        return result