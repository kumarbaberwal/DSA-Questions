"""
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.
 

Example 1:

Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
Example 2:

Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.

"""

class Solution:
    def threeConsecutiveOdds(self, arr: list[int]) -> bool:
        for i in range(2, len(arr)):
            if arr[i - 2] % 2 != 0 and arr[i - 1] % 2 !=0 and arr[i] % 2 != 0:
                return True
            
        return False
    
if __name__ == "__main__":
    sol = Solution()
    arr = [2,6,4,1]
    # arr = [1,2,34,3,4,5,7,23,12]
    print(sol.threeConsecutiveOdds(arr))