class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                val = board[r][c]
                box_key = (r // 3, c // 3)

                if val in rows.get(r, set()) or val in cols.get(c, set()) or val in boxes.get((r//3, c//3), set()):
                    return False

                rows.setdefault(r, set()).add(val)
                cols.setdefault(c, set()).add(val)
                boxes.setdefault(box_key, set()).add(val)
        
        return True