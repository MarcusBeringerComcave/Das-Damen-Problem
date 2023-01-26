def solve_n_queens(n):
    def is_valid(board, row, col):
        for i in range(row):
            if board[i] == col or \
               abs(board[i] - col) == abs(i - row):
                return False
        return True

    def backtrack(board, row):
        if row == n:
            result.append(board[:])
            return 
        for col in range(n):
            if is_valid(board, row, col):
                board[row] = col
                backtrack(board, row + 1)

    result = []
    backtrack([-1] * n, 0)
    return result
