class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)       
        cols = len(grid[0])
        for i in range(0,rows):
            for j in range(0,cols):
                if grid[i][j]==0:
                    queue.append((i,j,0))
        while len(queue)!=0:
            i,j,distance=queue.popleft()
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i, new_j = i+dx, j+dy
                if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] != 2147483647:
                    continue      
                grid[new_i][new_j] = distance+1
                queue.append((new_i, new_j, distance + 1))
        

        

