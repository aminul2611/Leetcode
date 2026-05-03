class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        return goal in (s + s)
s = input("Enter s: ")
goal = input("Enter goal: ")

sol = Solution()
print(sol.rotateString(s, goal))