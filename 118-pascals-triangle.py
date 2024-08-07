"""

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

"""

class Solution:
    def triangle(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        
        for i in range(numRows - 1):
            temp = [0] + result[-1] + [0]
            result += [[temp[j] + temp[j + 1] for j in range(len(temp) - 1)]]
        return result
        
if __name__ == "__main__":
    s = Solution()
    print(s.triangle(5))