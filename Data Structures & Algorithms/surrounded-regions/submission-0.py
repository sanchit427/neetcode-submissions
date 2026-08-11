class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row= len(board)
        col= len(board[0])
        queue=deque()
        visted=[[0]*col  for _ in range(row)]
        for i in range (0,row) :
            for j in range(0,col):
                if i ==0 or j==0 or i ==row-1 or j==col-1:
                    if board[i][j]=="O":
                        queue.append((i,j))
        while len(queue)!=0:
            i,j=queue.popleft()
            visted[i][j]=1
            for dx,dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                new_i,new_j=i+dx,j+dy
                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= col:
                    continue
                if board[new_i][new_j]=="X":
                    continue
                if visted[new_i][new_j]==0:
                    queue.append((new_i,new_j))
                    visted[new_i][new_j]=1
        for i in range (0,row) :
            for j in range(0,col):
                if board[i][j]=="O" and visted[i][j]==0:
                    board[i][j]="X"
        



        