class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        row=len(grid)
        cols=len(grid[0])
        rem=0
        distance=0
        for i in range(0,row):
            for j in range (0,cols):
                if grid[i][j]==1:
                    rem+=1
                if grid [i][j]==2:
                    queue.append((i,j,0))
        while len(queue)!=0 :
            r, c, distance = queue.popleft()
            for dx, dy in [(1,0),(0,1),(-1,0),(0,-1)]:
                new_i, new_j = r+dx, c+dy
                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= cols:
                    continue
                if grid[new_i][new_j] !=1:  # skip walls and already filled
                    continue
                rem-=1
                grid[new_i][new_j]=2
                queue.append((new_i,new_j,distance+1))
        if rem==0:
            return distance
        else:
            return -1

       

            


        