class Solution(object):
    def maxPathScore(Self, grid, k):
        m = len(grid)
        n = len(grid[0])
        dp =[[[-1 for _ in range(k +1)] for _ in range(n)] for _ in range(m)]

        dp[0][0][0] = 0

        for i in range(m):
            for j in range(n):
                for c in range(k+1):
                    if dp[i][j][c] == -1:
                         continue

                    for di, dj in [(0, 1), (1,0)]:
                        ni, nj = i + di, j + dj
                   
                        if 0 <= ni < m and 0 <= nj < n:
                            val = grid[ni][nj]
                            move_cost = 1 if val > 0 else 0
                            new_cost = c + move_cost

                            if new_cost <= k:
                                new_score = dp[i][j][c] + val
                                if new_score > dp[ni][nj][new_cost]: 
                                    dp[ni][nj][new_cost] = new_score

        ans = -1
        for c in range(k +1):
            if dp[m-1][n-1][c] > ans:
                 ans = dp[m - 1][n - 1][c]
        return ans