class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(i for i in s if i.isalnum()).lower()
        rev = [] * len(s)
        for i in reversed(s):
            rev.append(i)
        return s == ''.join(rev)
