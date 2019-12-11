from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        result = [0 for _ in range(len(queries))]

        queries_frequencies = [q.count(min(q)) for q in queries]
        words_frequencies = [w.count(min(w)) for w in words]

        for i in range(len(queries_frequencies)):
            for w in words_frequencies:
                if queries_frequencies[i] < w:
                    result[i] += 1

        return result


solution = Solution()
assert [1, 2] == solution.numSmallerByFrequency(["bbb", "cc"], ["a", "aa", "aaa", "aaaa"])
assert [1] == solution.numSmallerByFrequency(["cbd"], ["zaaaz"])
assert [6, 1, 1, 2, 3, 3, 3, 1, 3, 2] == solution.numSmallerByFrequency(
    ["bba", "abaaaaaa", "aaaaaa", "bbabbabaab", "aba", "aa", "baab", "bbbbbb", "aab", "bbabbaabb"],
    ["aaabbb", "aab", "babbab", "babbbb", "b", "bbbbbbbbab", "a", "bbbbbbbbbb", "baaabbaab", "aa"])
