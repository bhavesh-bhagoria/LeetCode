class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)
        reverse = ""
        for i in range(len(string_x)-1,-1,-1):
            reverse +=string_x[i]
        if reverse == string_x and x >= 0 :
            return True
        else:
            return False
                