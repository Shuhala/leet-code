class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True

        string = [c for c in s.lower() if c.isalpha() or c.isalnum()]
        return list(reversed(string)) == string


solution = Solution()
assert solution.isPalindrome("A man, a plan, a canal: Panama") is True
assert solution.isPalindrome("race a car") is False
assert solution.isPalindrome("0P") is False
