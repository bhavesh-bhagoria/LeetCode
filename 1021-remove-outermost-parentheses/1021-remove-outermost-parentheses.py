class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        count = 0
        start = 0

        for i in range(len(s)):
            if s[i] == '(':
                count += 1
            else:
                count -= 1

            if count == 0:
                for j in range(start + 1, i):
                    ans += s[j]

                start = i + 1

        return ans