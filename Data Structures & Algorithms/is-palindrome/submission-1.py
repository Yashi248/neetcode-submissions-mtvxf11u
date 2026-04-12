class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        n = len(s)
        for i in range(n):
            j = n - i - 1
            if s[i].lower() != s[j].lower():
                return False
        return True
