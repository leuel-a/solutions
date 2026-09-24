from typing import List

class Solution:
    def getDigitSum(self, num: int) -> int:
        return sum([int(value) for value in str(num)])


    def smallestIndex(self, nums: List[int]) -> int:
        for index, num in enumerate(nums):
            if self.getDigitSum(num) == index:
                return index
        return -1
