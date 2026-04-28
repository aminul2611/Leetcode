class Solution(object):
    def minOperations(self, grid, x):
        
        arr = []
        for row in grid:
            for num in row:
                arr.append(num)
        
        remainder = arr[0] % x
        for num in arr:
            if num % x != remainder:
                return -1
        
        arr.sort()
        
        median = arr[len(arr) // 2]
        
        operations = 0
        for num in arr:
            operations += abs(num - median) // x
        
        return operations
    
if __name__ == "__main__":
    m, n = map(int, input("Enter rows and cols: ").split())
    
    grid = []
    print("Enter grid row by row:")
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)
    
    x = int(input("Enter x: "))
    
    sol = Solution()
    result = sol.minOperations(grid, x)
    
    print("Output:", result)