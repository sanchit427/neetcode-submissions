class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited=[0]*n
        queue=deque()
        adj_list=[[]for _ in range(n)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        queue.append((0,-1))
        visited[0]=1
        while len(queue)!=0:
            node,parent=queue.popleft()
            for neigh in adj_list[node]:
                if visited[neigh]==0:
                    visited[neigh]=1
                    queue.append((neigh,node))
                else:
                    if neigh==parent:
                        continue
                    else:
                        return False
        for i in visited:
            if i==0:
                return False
        return True

        