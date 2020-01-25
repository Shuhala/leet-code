class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}

        num_of_chars = len(s)

        for i in range(num_of_chars):
            # s key not in mapping and t was not mapped to something else
            if s[i] not in mapping.keys() and t[i] not in mapping.values():
                mapping[s[i]] = t[i]
            elif t[i] != mapping.get(s[i]):
                # t is not mapped or to another s key
                return False

        return True


solution = Solution()
assert solution.isIsomorphic("egg", "add") is True
assert solution.isIsomorphic("foo", "bar") is False
assert solution.isIsomorphic("paper", "title") is True
