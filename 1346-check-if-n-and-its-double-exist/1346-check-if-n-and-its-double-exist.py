class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i, element in enumerate(arr):
            for j, el in enumerate(arr):
                if element == 2 * el and i != j and 0 <= i and j < len(arr):
                    return True
                else:
                    continue
        return False