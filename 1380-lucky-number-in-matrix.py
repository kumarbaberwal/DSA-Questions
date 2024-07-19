"""
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
"""

class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        m = len(matrix)
        n = len(matrix[0])
        rowMin = []

        for i in range(m):
            rMin = float('inf')
            for j in range(n):
                rMin = min(rMin, matrix[i][j])
            rowMin.append(rMin)

        colMax = []
        for i in range(n):
            cMax = float('-inf')
            for j in range(m):
                cMax = max(cMax, matrix[j][i])
            colMax.append(cMax)
        luckyNumber = []

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumber.append(rowMin[i])
        
        return luckyNumber
        
        
if __name__ == "__main__":
    import numpy
    sol = Solution()
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
    matrix = [[7,8],[1,2]]
    matrix = [[3,6],[7,1],[5,2],[4,8]]
    # print(numpy.transpose(matrix))
    print(f"The Lucky Number is : {sol.luckyNumbers(matrix=matrix)}")
    # m = len(matrix)
    # print(m)
    # n = len(matrix[0])
    # print(n)
    # sr = []
    # for i in range(m):
    #     matrix[i].sort
    #     sr.append(matrix[i][0])
    # print(sr)
    # sc = []
    # import numpy
    # trans = numpy.transpose(matrix)
    # for j in range(n):
    #     trans[j].sort()
    #     sc.append(trans[j][-1])

    # print(sc)
    # result = []
    # for r in sr:
    #     for c in sc:
    #         if r == c:
    #             result.append(r)
    # print(result)