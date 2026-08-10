class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        column=len(grid[0])
        visted= [[0] * column for _ in range(row)] 
        reslut=[]
        def dsf(i,j):
            nonlocal count
            visted[i][j]=1
            for dx,dy in [(0,1),(-1,0),(0,-1),(1,0)]:
                new_i,new_j=i+dx,j+dy
                if new_i<0 or new_i>=row or new_j<0 or new_j>=column:
                    continue
                if grid[new_i][new_j]==0:
                    continue
                if visted[new_i][new_j] == 1:  
                    continue
                
                count+=1
                dsf(new_i,new_j)
            
        for i in range(0,row):
            for j in range(0,column):
                if grid[i][j]==0:
                    continue
                if visted[i][j]==1:
                    continue
                visted[i][j]=1
                count=1
                dsf(i,j)
                reslut.append(count)
        return  max(reslut) if reslut else 0
                
                
        