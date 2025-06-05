class Solution(object):
    def checkSubBox(sef, board, num, row, col):
        startRow = row // 3 * 3
        startCol = col // 3 * 3
        for i in range(startRow, startRow+3):
            for j in range(startCol, startCol+3):
                if i != row and j != col and board[i][j] == num:
                    return False
        return True

    def checkRowCol(self, board, num, row, col):
        for i in range(9):
            if i != col and board[row][i] == num or i != row and board[i][col] == num:
                return False
        return True

    def isValidSudoku(self, board):
        for row in range(len(board)):
            for col in range(len(board)):
                # filter all the False possibilities first
                if board[row][col] == ".":
                    continue
                # check other posibilities require detail checking
                if not self.checkRowCol(board, board[row][col], row, col) or not self.checkSubBox(board, board[row][col], row, col):
                    return False
        return True

    # use "Set"

    # def isValidSudoku(self, board):
    #     # practice using tuple, SET
    #     # rowSet, colSet, subboxSet

def main():
    sol = Solution()
    board = [["8","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(sol.isValidSudoku(board))

if __name__ == "__main__":
    main()