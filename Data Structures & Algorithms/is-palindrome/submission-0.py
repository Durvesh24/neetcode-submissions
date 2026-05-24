class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join([c.lower() for c in s if c.isalnum()])

        return s1[::-1] == s1