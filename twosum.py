from itertools import combinations

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


def twoSum(nums_list: list, tgt: int) -> list:

    def get_index(t1, test_tgt):
        return t1 if sum(t1) == test_tgt else None

    return [list(e) for e in list(map(lambda x: get_index(x, tgt), combinations(nums_list, 2))) if e is not None][0]


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))

nums = [3, 2, 4]
target = 6

print(twoSum(nums, target))
