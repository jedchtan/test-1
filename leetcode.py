from collections import deque

# BFS for graphs: num of islands

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def bfs(r,c):
            q = deque()
            q.append((r,c))

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    newr = dr + r
                    newc = dc + c
                    if (newr<0 or newc<0 or newr==ROWS or newc==COLS or (newr,newc) in visited or grid[newr][newc] == '0'):
                        continue

                    visited.add((newr,newc))
                    q.append((newr,newc))
        
        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)
                            



