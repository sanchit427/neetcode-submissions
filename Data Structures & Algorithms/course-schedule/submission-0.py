class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        queue = deque()
        result = []
        adj_list = [[] for _ in range(numCourses)]

        for u, v in prerequisites:
            adj_list[v].append(u)
            indegree[u] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            result.append(node)

            for neigh in adj_list[node]:
                indegree[neigh] -= 1

                if indegree[neigh] == 0:
                    queue.append(neigh)

        return len(result) == numCourses