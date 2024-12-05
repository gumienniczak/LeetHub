class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        
        # If both strings have different counts of L, R, or _, they cannot match
        if start.replace('_', '') != target.replace('_', ''):
            return False
        
        # Iterate through both strings and check the movement feasibility of L and R
        start_index = target_index = 0
        
        while start_index < n and target_index < n:
            # Skip underscores in both start and target
            while start_index < n and start[start_index] == '_':
                start_index += 1
            while target_index < n and target[target_index] == '_':
                target_index += 1
            
            # If both reached the end or both have characters that don't match, return False
            if start_index < n and target_index < n:
                if start[start_index] != target[target_index]:
                    return False
                
                # If it's 'L', it must move left in target, so ensure start's L can reach target's L
                if start[start_index] == 'L':
                    if start_index < target_index:
                        return False
                
                # If it's 'R', it must move right in target, so ensure start's R can reach target's R
                if start[start_index] == 'R':
                    if start_index > target_index:
                        return False
                
                # Move both indices forward
                start_index += 1
                target_index += 1
        
        return True