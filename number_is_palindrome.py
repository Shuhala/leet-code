class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == "".join(reversed(str(x)))


solution = Solution()
assert solution.isPalindrome(121) is True
assert solution.isPalindrome(-121) is False
assert solution.isPalindrome(10) is False
