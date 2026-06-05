class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 0
        new_array = set(nums)
        start_nums = []
        for num in new_array:
            if num - 1 in new_array:
                continue
            start_nums.append(num)
        
        for num in start_nums:
            current_num = num
            current_streak = 1

            while current_num + 1 in new_array:
                current_streak += 1
                current_num += 1
            
            counter = max(counter, current_streak)
        return counter

                

        




        
        
        

        
