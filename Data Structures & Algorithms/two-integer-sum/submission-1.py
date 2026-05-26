class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        u = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in u:
                return [u[difference], i]
            elif difference not in u:
                u[nums[i]] = i

        