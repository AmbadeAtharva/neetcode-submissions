class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [[0,1], [0,-1], [-1,0], [1,0]]

        def bfs(r,c):
            
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            
            while q:
                row, col = q.popleft()

                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr in range(rows) and nc in range(cols) and grid[nr][nc]=='1' and (nr,nc) not in visited):

                        visited.add((nr,nc))
                        q.append((nr,nc))





        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i,j) not in visited:
                    bfs(i,j)
                    islands += 1

        return islands


