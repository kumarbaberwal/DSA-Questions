"""
A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.

 

Example 1:
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1st, so it is the 1st distinct string.
"a" appears 2nd, so it is the 2nd distinct string.
Since k == 2, "a" is returned. 

Example 2:
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1st string "aaa" is returned.

Example 3:
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".

"""

class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        from collections import defaultdict
        count = defaultdict(int)
        for i in arr:
            count[i] += 1
        
        for key in count:
            if count[key] == 1:
                k -= 1
            if k == 0:
                return key
        return ""
        



        # distinct = []
        # for i in arr:
        #     if arr.count(i) == 1:
        #         distinct.append(i)
        # if len(distinct) < k:
        #     return ""
        # else:
        #     return distinct[k-1]


if __name__ == "__main__":
    obj = Solution()
    arr = ["d","b","c","b","c","a"]
    k = 2
    print(obj.kthDistinct(arr,k))