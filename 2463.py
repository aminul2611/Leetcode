import sys

class Solution:
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        n = len(robot)
        m = len(factory)

        sys.setrecursionlimit(10**7)

        memo = {}

        def dp(i, j):
            if i == n:
                return 0
            if j == m:
                return float('inf')

            if (i, j) in memo:
                return memo[(i, j)]

            res = dp(i, j + 1)

            pos, limit = factory[j]

            total = 0

            for k in range(1, min(limit, n - i) + 1):
                total += abs(robot[i + k - 1] - pos)
                res = min(res, total + dp(i + k, j + 1))

            memo[(i, j)] = res
            return res

        return dp(0, 0)