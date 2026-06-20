class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            a = [board[i][j] for j in range(9) if board[i][j] != "."]
            if len(a) != len(set(a)): return False

            a = [board[j][i] for j in range(9) if board[j][i] != "."]
            if len(a) != len(set(a)): return False

            a = [board[i//3*3 + j//3][3*(i%3) + j%3] for j in range(9) if board[i//3*3 + j//3][3*(i%3) + j%3] != "."]
            if len(a) != len(set(a)): return False
        return True