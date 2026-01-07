class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]

        for i in range(len(first)):
            for word in strs[1:]:
                # If index exceeds word length OR characters mismatch
                if i >= len(word) or word[i] != first[i]:
                    return first[:i]

        return first
