"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]

"""

class Solution:
    def sortColors(self, nums: list[int]) -> list[int]:
        l, r = 0, len(nums) - 1
        i = 0
        while i <= r:
            if nums[i] == 0:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            elif nums[i] == 2:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            i += 1


        # from collections import Counter
        # count = Counter(nums)
        # # nums =  [0] * count[0] + [1] * count[1] + [2] * count[2]

        # j = 0
        # for i in range(count[0]):
        #     nums[j + i] = 0
        
        # j += count[0]
        # for i in range(count[1]):
        #     nums[j + i] = 1

        # j += count[1]
        # for i in range(count[2]):
        #     nums[j + i] = 2
        return nums
if __name__ == "__main__":
    nums = [2,0,2,1,1,0]
    from collections import Counter
    count = Counter(nums)
    # nums = [0] * count[0] + [1] * count[1] + [2] * count[2]
    # nums =  list([0] * count[0] + [1] * count[1] + [2] * count[2])
    # print(nums)
    print(Solution().sortColors(nums))    
