class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        x_c = x

        while x:
            digit = x % 10
            x = x // 10
            reversed_x = reversed_x * 10 + digit

        return reversed_x == x_c