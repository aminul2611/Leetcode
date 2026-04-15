class Solution(object):
    def minimumTotalDistance(self, robot, factory):
        robot.sort()
        factory.sort()

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, j):
            if i == len(robot):
                return 0
            
            if j == len(factory):
                return float('inf')

            res = dp(i, j + 1)

            pos, limit = factory[j]
            total = 0

            for k in range(1, limit + 1):
                if i + k - 1 >= len(robot):
                    break

                total += abs(robot[i + k - 1] - pos)
                res = min(res, total + dp(i + k, j + 1))

            return res

        return dp(0, 0)


if __name__ == "__main__":
    robot = list(map(int, input("Enter robots: ").split()))
    
    n = int(input("Number of factories: "))
    factory = []

    for _ in range(n):
        pos, limit = map(int, input("Enter factory position and limit: ").split())
        factory.append([pos, limit])

    sol = Solution()
    result = sol.minimumTotalDistance(robot, factory)

    print("Minimum Distance:", result)