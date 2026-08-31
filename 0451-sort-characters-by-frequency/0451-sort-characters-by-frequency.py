class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        # For s = "tree":
        # freq = {'t': 1, 'r': 1, 'e': 2}
        # sorted_char = [('e', 2), ('t', 1), ('r', 1)]
        #
        # sorted() takes O(k log k) time because it uses a comparison-based
        # sorting algorithm (Timsort). Here k = number of unique characters.
        # Since k <= n (length of s), worst case is O(n log n).
        sorted_char = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        final = ""

        for key, value in sorted_char:
            final = final + (key * value)

        return final