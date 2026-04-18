class Solution(object): 
    def mirrorDistance(self, n):
        rev = int(str(n)[::-1])
        return abs(n-rev)
    
sol = Solution()

while True:
    n = int(input("Enter a number: "))
    print(sol.mirrorDistance(n))