#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        r = 0 
        while x > 0:
            r *= 10
            r += x % 10
            x /= 10
        return x == r

# @lc code=end/

