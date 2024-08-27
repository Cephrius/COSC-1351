#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # init left and right boundaries
        left = 0
        right = len(nums) - 1
        
        # while loop
        
        while left < right:
            # finding mid index
            mid = (left + right) // 2
            # if mid is target
            if nums[mid] >= target:
                right = mid
            else: 
                left = mid + 1
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1
# @lc code=end

