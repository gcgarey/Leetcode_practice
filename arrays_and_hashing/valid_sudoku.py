# Leetcode 36: is Valid Sudoku
from collections import defaultdict

def isValidSudoku(board) -> bool:
    #{# -> set}
    rows = defaultdict(set)
    columns = defaultdict(set)
    boxes = defaultdict(set)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if board[r][c] in rows[r] or board[r][c] in columns[c] or board[r][c] in boxes[r // 3, c // 3]:
                return False
            rows[r].add(board[r][c])
            columns[c].add(board[r][c])
            boxes[(r // 3, c // 3)].add(board[r][c])

    return True
