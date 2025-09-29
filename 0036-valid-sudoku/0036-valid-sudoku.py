class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        N = len(board)
        M = len(board[0])

        for i in range(N):
            row = set()
            for j in range(M):
                if board[i][j] in row:
                    return False
                if board[i][j] != ".":
                    row.add(board[i][j])

        for i in range(N):
            col = set()
            for j in range(M):
                if board[j][i] in col:
                    return False
                if board[j][i] != ".":
                    col.add(board[j][i])

        starts = [(0,0), (0,3), (0,6),
                (3, 0), (3,3), (3, 6),
                (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            box = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    if board[row][col] in box:
                        return False
                    if board[row][col] != ".":
                        box.add(board[row][col])
        

        return True


