# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.


import timeit

# Example 1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3
# Input: nums = [3,3], target = 6
# Output: [0,1]



# My solution 1
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for element_out in range(0, len(nums)):
#             for element_in in range(element_out + 1, len(nums)):
#                 if nums[element_out] + nums[element_in] == target:
#                     return [element_out, element_in]




# My solution 2 - 2 pointer technique
# from typing import List
#
#
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         x = 0
#         y = len(nums) - 1
#         for _ in range(0, len(nums)):
#             if nums[x] + nums[y] == target:
#                 return [nums[x], nums[y]]
#             elif nums[x] + nums[y] < target:
#                 x += 1
#             elif nums[x] + nums[y] > target:
#                 y -= 1
#
# resenje = Solution()
# print(resenje.twoSum([-1,1,2,3,5,9,14,58], 11))


# Now, let's compare the time of the 2 techniques
# On my computer, the 2 pointer technique took 0.026281300000000007 seconds
# On the other hand, the 2 loops technique took 34.136024 seconds.
# Let's see...


# The 2 pointer technique
# brojevi = []
# for i in range(1,10_000):
#     brojevi.append(random.randint(1,100_000_000))
# brojevi.sort()
#
# import timeit
#
# t = timeit.Timer(lambda:resenje.twoSum(brojevi, 11))
#
# print(t.timeit(10))




# The 2 for loop technique
# resenje2 = Solution()
# print(resenje2.twoSum([-1,1,2,3,5,9,14,58], 11))
#
# brojevi = []
# for i in range(1,10_000):
#     brojevi.append(random.randint(1,100_000_000))
# brojevi.sort()
#
# import timeit
#
# t = timeit.Timer(lambda:resenje2.twoSum(brojevi, 11))
#
# print(t.timeit(10))
