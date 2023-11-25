nums = [2, 7, 11, 15, 2]
target = 4


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        res = []
        for item in nums:
            for elem in nums:
                if item + elem == target and nums.index(item) != nums.index(elem):
                    res.append(nums.index(item))
                    res.append(nums.index(elem))
                    return res
                elif item + elem == target and nums.index(item) == nums.index(elem) and nums.count(item) == 2:
                    # x[0] - индекс числа х, x[1] - значение числа х
                    res = [x[0] for x in enumerate(nums) if x[1] == item]
                    return res


evaluate = Solution()
print(evaluate.twoSum(nums, target))
