class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set()for _ in range(9)]
        col=[set()for _ in range(9)]
        subbox=[set()for _ in range(9)]
        for i in range(9):
            for j in range(9):
                val=board[i][j]
                if val==".":
                    continue 
                index=(i // 3) * 3 + (j // 3)
                if val in rows[i] or val in col[j] or val in subbox[index]:
                    return False
                rows[i].add(val)
                col[j].add(val)
                subbox[index].add(val)
        return True




