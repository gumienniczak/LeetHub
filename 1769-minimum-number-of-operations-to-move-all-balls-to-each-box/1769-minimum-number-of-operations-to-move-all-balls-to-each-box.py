class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        for current_box in range(n):
            if boxes[current_box] == '0':
                continue
            else:
                for new_position in range(n):
                    result[new_position] += abs(new_position - current_box)
        return result 