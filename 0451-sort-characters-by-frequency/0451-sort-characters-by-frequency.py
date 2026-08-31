class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1

        sorted_char = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        final = ""

        for key, value in sorted_char:
            final = final + (key * value)

        return final