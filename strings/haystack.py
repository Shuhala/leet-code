class Solution:
    """
    Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i

        return -1


solution = Solution()
assert 2 == solution.strStr("hello", "ll")
assert -1 == solution.strStr("aaaaa", "bba")
assert 0 == solution.strStr("aaaaa", "")
