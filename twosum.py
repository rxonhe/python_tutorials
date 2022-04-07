from itertools import combinations


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
