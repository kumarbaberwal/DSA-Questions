"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        setNums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in setNums:
                large = 0
                while num + large in setNums:
                    large += 1
                longest = max(large, longest)
        return longest


            



if __name__ == "__main__":
    sol = Solution()
    nums = [100,4,200,1,3,2,10,11, 12, 13, 14, 15, 16]
    # nums = []
    # nums = [1,2,0,1]
    print(f"The longest consecutive sequence is of lenght: {sol.longestConsecutive(nums=nums)}")