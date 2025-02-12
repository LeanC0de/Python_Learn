class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []


A1 = [2, 3, 4, 5, 5, 6, 7, 8]
A2 = 11
print(Solution().twoSum(A1, A2))
