class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        row = len(heights)
        col = len(heights[0])

        queue1 = deque()
        queue2 = deque()

        pacific = set()
        atlantic = set()

        # Initial border cells
        for i in range(row):
            for j in range(col):

                if i == 0 or j == 0:
                    queue1.append((i, j))
                    pacific.add((i, j))

                if i == row - 1 or j == col - 1:
                    queue2.append((i, j))
                    atlantic.add((i, j))

        # Pacific BFS
        while queue1:
            i, j = queue1.popleft()

            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:

                new_i = i + dx
                new_j = j + dy

                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= col:
                    continue

                if ((new_i, new_j) not in pacific and
                    heights[new_i][new_j] >= heights[i][j]):

                    pacific.add((new_i, new_j))
                    queue1.append((new_i, new_j))

        # Atlantic BFS
        while queue2:
            i, j = queue2.popleft()

            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:

                new_i = i + dx
                new_j = j + dy

                if new_i < 0 or new_i >= row or new_j < 0 or new_j >= col:
                    continue

                if ((new_i, new_j) not in atlantic and
                    heights[new_i][new_j] >= heights[i][j]):

                    atlantic.add((new_i, new_j))
                    queue2.append((new_i, new_j))

        
        result = pacific & atlantic

        return [[r, c] for r, c in result]