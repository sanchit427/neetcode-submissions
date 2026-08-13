class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=[0]*n
        queue=deque()
        count=0
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        for i in range(0,n):
            if visited[i]==0:
                count+=1
                queue.append(i)
                visited[i]=1
                while len(queue)!=0:
                    node=queue.popleft()
                    for neigh in adj[node]:
                        if visited[neigh]==0:
                            visited[neigh]=1
                            queue.append(neigh)
                        else:
                            continue
        return count
        