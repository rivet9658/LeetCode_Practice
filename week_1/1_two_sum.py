# package import
from typing import List


class Solution:
    # my first answer
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        x = 0
        y = 1
        while nums[x] + nums[y] != target:
            y += 1
            if y >= len(nums):
                x += 1
                y = x + 1
                if x >= len(nums) - 1:
                    return [0, 0]
        return [x, y]

    # great answer
    def great_two_sum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # fast answer
    def fast_two_sum(self, nums: List[int], target: int) -> List[int]:
        while len(nums) > 1:
            num = nums.pop()
            if target - num in nums:
                return [len(nums), nums.index(target - num)]
