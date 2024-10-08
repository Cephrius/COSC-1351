#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reversed_num = 0
        original_num = x
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10
        return reversed_num == original_num


            
# @lc code=end

