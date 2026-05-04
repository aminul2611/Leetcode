class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()

while True:
    s = input("Enter the Row: ").strip()

    if s.lower() == "exit":
        break
    s = s[1: -1]
    rows = s.split("],")

    matrix = []


    for row in rows:
        row = row.replace("[", "").replace("]","")
        if row:
            nums = list(map(int, row.split(",")))
            matrix.append(nums)

    sol = Solution()
    sol.rotate(matrix)

    print("Rotated matrix: ")
    print(matrix)