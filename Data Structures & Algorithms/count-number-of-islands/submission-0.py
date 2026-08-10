class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row = len(grid)
        column = len(grid[0])
        
        deep_copy = [[0 for _ in range(column)] for _ in range(row)]
        count = 0

        def dsf(i, j):
            deep_copy[i][j] = count
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_i, new_j = i + dx, j + dy
                if new_i < 0 or new_j < 0 or new_i >= row or new_j >= column:
                    continue
                
                if grid[new_i][new_j] == "0" or deep_copy[new_i][new_j] != 0:
                    continue
                dsf(new_i, new_j)

        for i in range(row):
            for j in range(column):
                
                if grid[i][j] == "0" or deep_copy[i][j] != 0:
                    continue 
                else:
                    count += 1
                    dsf(i, j)

        
        return count