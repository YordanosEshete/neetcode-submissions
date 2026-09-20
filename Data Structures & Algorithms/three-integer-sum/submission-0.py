class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        

        for i in range(len(nums)):
            a = nums[i]
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            j = i + 1
            
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] == -nums[i]:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif nums[j] + nums[k] > -nums[i]:
                    k -= 1
                elif nums[j] + nums[k] < -nums[i]:
                    j += 1

        return ans
                






            