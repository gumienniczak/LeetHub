class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        original = [row[:] for row in matrix]
        max_counter = len(matrix) - 1
        for r in range(len(matrix)):
            for c in range(len(matrix)):
                min_counter = c
                matrix[min_counter][max_counter] = original[r][c]
            max_counter -= 1

                