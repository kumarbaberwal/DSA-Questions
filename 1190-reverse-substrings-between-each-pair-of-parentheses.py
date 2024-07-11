"""You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string."""


def reverseParentheses(s: str) -> str:
    stack = []
    for char in s:
        if char == ')':
            rev = ''
            while stack and stack[-1] != '(':
                rev += stack.pop()
            if stack:
                stack.pop()
            for c in rev:
                stack.append(c)
        else:
            stack.append(char)
    return ''.join(stack)

if __name__ == "__main__":
    s = "(abcd)"
    s1 = "(u(love)i)"
    s2 = "(ed(et(oc))el)"
    print(f"The reversed string is : {reverseParentheses(s)}") 
    print(f"The reversed string is : {reverseParentheses(s1)}") 
    print(f"The reversed string is : {reverseParentheses(s2)}") 