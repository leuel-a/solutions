class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        occurrence = [0] * 101

        for num in nums:
            occurrence[num] += 1

        result = []
        for _ in range(len(nums)):
            for i in range(1, 101):
                if occurrence[i] != 0:
                    result.append(i)
                    occurrence[i] -= 1
        return result
