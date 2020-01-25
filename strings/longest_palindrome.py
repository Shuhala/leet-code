class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i in range(len(s)):
            for j in reversed(range(i, len(s) + 1)):
                if s[i:j] == s[i:j][::-1] and len(s[i:j]) > len(longest):
                    longest = s[i:j]
                    if j == len(s):
                        return longest

        return longest


solution = Solution()
assert "bab" == solution.longestPalindrome("babad")
assert "bb" == solution.longestPalindrome("cbbd")
assert "bb" == solution.longestPalindrome("bb")
assert "a" == solution.longestPalindrome("a")
assert "" == solution.longestPalindrome("")
assert "bacab" == solution.longestPalindrome("abacab")
