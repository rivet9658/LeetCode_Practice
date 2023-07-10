class Solution:
    # my first answer
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        if len(s) == 0:
            return True
        split = len(s) // 2
        start = s[:split]
        if len(s) % 2 == 0:
            end = s[split:]
        else:
            end = s[split + 1:]
        end = end[::-1]
        if start == end:
            return True
        else:
            return False
