"""

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) :
        dict = {}
        fre = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        
        for n, c in dict.items():
            fre[c].append(n)

        elements = []
        for i in range(len(nums) - 1, 0, -1):
            for f in fre[i]:
                elements.append(f)
                if len(elements) == k:
                    return elements


if __name__ == "__main__":
    solution = Solution()
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"The most frequent elements are : {solution.topKFrequent(nums, k)}")
    # dicte = {1:1}
    # if 1 not in dicte.keys():
    #     print(False)
    # else:
    #     print(True)
    # print(dicte[1])
