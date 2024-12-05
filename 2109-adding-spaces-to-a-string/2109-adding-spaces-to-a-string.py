class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        indices = sorted(spaces)
        indices = [0] + indices + [len(s)]
        parts = [s[indices[i]:indices[i+1]] for i in range(len(indices) - 1)]
        return ' '.join(parts)