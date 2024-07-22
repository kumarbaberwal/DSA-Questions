"""
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

"""

class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return [name for height, name in reversed(sorted(zip(heights, names)))]
    
        # height_to_names = {height: name for height, name in zip(heights, names)}
        
        # return [height_to_names[height] for height in reversed(sorted(height_to_names.keys()))]


        # for i in range(len(heights)):
        #     max = heights[i]
        #     j = i
        #     for k in range(i, len(heights)):
        #         if heights[k] > max:
        #             max = heights[k]
        #             j = k
        #     if j != i:
        #         heights[i], heights[j] = heights[j], heights[i]
        #         names[i], names[j] = names[j], names[i]
        # return names

if __name__ == "__main__":
    sol = Solution()
    names = ["Mary","John","Emma"]
    heights = [180,165,170]
    print(f"Sorted Names in descending order: {sol.sortPeople(names, heights)}")