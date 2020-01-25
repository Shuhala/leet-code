class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        if len(set(s)) == 1:
            return 1

        longest = 0
        start, end = 0, 1
        while end < len(s):
            if s[end] in s[start:end]:
                # duplicate, move start to duplicate index
                start += s[start:end].index(s[end]) + 1

            if end - start + 1 > longest:
                longest = end - start + 1

            end += 1

        return longest


solution = Solution()
assert 3 == solution.lengthOfLongestSubstring("abcabcbb")
# assert 1 == solution.lengthOfLongestSubstring("bbbbb")
assert 3 == solution.lengthOfLongestSubstring("pwwkew")
