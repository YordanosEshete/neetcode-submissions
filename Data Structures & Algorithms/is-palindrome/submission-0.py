class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]

        