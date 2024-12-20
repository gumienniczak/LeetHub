# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
    
        queue = deque([root])
        level = 0  # Start at level 0 (even)
    
        while queue:
            level_size = len(queue)
            current_level_values = []
        
            # Collect nodes at the current level
            for _ in range(level_size):
                node = queue.popleft()
                if level % 2 == 1:
                    current_level_values.append(node)
            
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            # Reverse and assign values for odd levels
            if level % 2 == 1:
                reversed_values = [node.val for node in reversed(current_level_values)]
                for node, new_val in zip(current_level_values, reversed_values):
                    node.val = new_val
        
            level += 1  # Move to the next level
    
        return root