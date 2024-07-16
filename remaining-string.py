"""

Given a string s without spaces, a character ch and an integer count. Your task is to return the substring that remains after the character ch has appeared count number of times.
Note:  Assume upper case and lower case alphabets are different. “”(Empty string) should be returned if it is not possible, or the remaining substring is empty.

Examples:

Input: s = "Thisisdemostring", ch = 'i', count = 3
Output: ng
Explanation: The remaining substring of s after the 3rd
occurrence of 'i' is "ng", hence the output is ng.

"""


class Solution:
    def printString(self, s, ch, count):
        i = 0
        j = 0
        while i < len(s) and j != count:
            if s[i] == ch:
                j += 1
            i += 1
            
        return s[i :]
     
if __name__ == "__main__":
    sol = Solution()
    s = "Thisisdemostring"
    ch = 'i'
    count = 3
    print(f'The remaining string is : {sol.printString(s, ch , count)}')

