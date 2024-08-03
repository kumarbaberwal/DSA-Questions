"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # with an approach of O(1) space complexity
        rows, cols = len(matrix), len(matrix[0])
        rowCol = 1

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0

                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        rowCol = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] =0
        if matrix[0][0] == 0:
            for i in range(rows):
                matrix[i][0] = 0
        if rowCol == 0 :
            for j in range(cols):
                matrix[0][j] =0


        # with an approach of O(m + n) space complexity
        # m = len(matrix)
        # n = len(matrix[0])
        # rows = set()
        # cols = set()
        # for i in range(m):
        #     for j in range(n):
        #         if matrix[i][j] == 0:
        #             rows.add(i)
        #             cols.add(j)
        
        # for i in range(m):
        #     for j in range(n):
        #         if i in rows or j in cols:
        #             matrix[i][j] = 0
                    




if __name__ == "__main__":
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    print(matrix)