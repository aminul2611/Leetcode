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
    