from collections import defaultdict
from typing import List
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        occurrences = defaultdict(int)
        paragraph_words = re.sub('[^a-zA-Z]+', ' ', paragraph.lower()).rsplit()
        for word in paragraph_words:
            if word not in banned:
                occurrences[word] += 1

        return max(occurrences, key=occurrences.get)


solution = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
assert "ball" == solution.mostCommonWord(paragraph, banned)
