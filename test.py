from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


A1 = [2, 3, 4, 5, 5, 6, 7, 8]
A2 = 11

A3 = Solution()
print(A3.twoSum(A1, A2))
