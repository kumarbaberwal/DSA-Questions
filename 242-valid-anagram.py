"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        s_dict = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            s_dict[char] += 1

        for char in t:
            if char not in s_dict or s_dict[char] == 0:
                return False
            
            s_dict[char] -= 1

        return True
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))