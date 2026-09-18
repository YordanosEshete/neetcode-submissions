class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        
        max_area = 0

        while left < right:
            width = right - left
            curr_area = min(heights[left], heights[right]) * width
            if curr_area > max_area:
                max_area = curr_area
            
            if min(heights[left], heights[right]) == heights[left]:
                left += 1
            else:
                right -= 1
        return max_area