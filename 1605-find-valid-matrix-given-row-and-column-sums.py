"""

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Example 2:

Input: rowSum = [5,7,10], colSum = [8,6,8]
Output: [[0,5,0],
         [6,1,0],
         [2,0,8]]
"""

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        rows, cols = len(rowSum), len(colSum)

        output = [[0] * cols for _ in range(rows)]
        
        i, j = 0, 0
        while i < rows and j < cols:
            output[i][j] = min(rowSum[i], colSum[j])

            rowSum[i] -= output[i][j]
            colSum[j] -= output[i][j]

            if rowSum[i] == 0:
                i += 1
            else:
                j += 1
        
        return output


if __name__ == "__main__":
    sol = Solution()
    rowSum = [5,7,10]
    colSum = [8,6,8]
    print(f'The matrix is : {sol.restoreMatrix(rowSum, colSum)}')
