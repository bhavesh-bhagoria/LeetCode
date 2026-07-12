class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word = ""
        for i in s:
            if i != " ":
                word += i
            else:
                if word != "":
                    words.append(word)
                    word = ""

        if word != "":
            words.append(word)

        words.reverse()
        ans = ""

        for j in range(len(words)):
            ans += words[j]
            if j != len(words) - 1:
                ans += " "

        return ans