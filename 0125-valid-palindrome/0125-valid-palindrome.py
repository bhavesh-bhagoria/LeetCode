class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for ch in s:
            ascii_val = ord(ch)
            if (65 <= ascii_val <= 90) or (97 <= ascii_val <= 122) or (48 <= ascii_val <= 57):
                filtered += ch.lower()
        reverse = ""
        for i in range(len(filtered) - 1, -1, -1):
            reverse += filtered[i]

        if filtered == reverse:
            return True
        else:
            return False
