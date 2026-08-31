class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)
        depth = 0
        maximum = 0
        for i in range(n):
            print(s[i])
            if s[i] == "(":
                depth +=1
                maximum = max(depth,maximum)
            if s[i] == ")":
                depth -=1
                maximum = max(depth,maximum)
        return maximum