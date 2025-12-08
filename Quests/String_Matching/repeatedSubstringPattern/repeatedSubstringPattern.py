class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)

        def check(p):
            if N % len(p) != 0:
                return False
            return p * (N // len(p)) == s

        for i in range(1, (N // 2) + 1):
            p = s[:i]

            if check(p):
                return True
        return False