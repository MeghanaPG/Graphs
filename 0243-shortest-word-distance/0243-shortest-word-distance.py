class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1_index = -1
        word2_index = -1
        min_distance = float('inf')  # Start with an infinitely large distance

        for i, word in enumerate(wordsDict):
            if word == word1:
                word1_index = i
            elif word == word2:
                word2_index = i

            if word1_index != -1 and word2_index != -1:
                min_distance = min(min_distance, abs(word1_index - word2_index))

        return min_distance