class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = sol[i-1][j-1] + sol[i-1][j]
            sol.append(row)
        return sol