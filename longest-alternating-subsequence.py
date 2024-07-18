"""
You are given an array arr. Your task is to find the longest length of a good sequence. A good sequence {x1, x2, .. xn} is an alternating sequence if its elements satisfy one of the following relations :

1.  x1 < x2 > x3 < x4 > x5. . . . . and so on
2.  x1 >x2 < x3 > x4 < x5. . . . . and so on

Examples:

Input: arr= [1, 5, 4]
Output: 3
Explanation: The entire sequenece is a good sequence.
Input: arr= [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
Output: 7
Explanation: There are several subsequences that achieve this length. 
One maximum length good subsequences is [1, 17, 10, 13, 10, 16, 8].
"""


class Solution:
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
        inc = 1
        dec = 1
        for i in range(1, len(arr)):
            if arr[i-1] < arr[i]:
                inc = dec + 1
            elif arr[i-1] > arr[i]:
                dec = inc + 1
        return max(inc, dec) if len(arr) > 0 else 0


if __name__  == "__main__":
    sol = Solution()
    arr = [1, 5, 4]
    arr= [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    print(f'The longest alternating subsequence is : {sol.alternatingMaxLength(arr)}')