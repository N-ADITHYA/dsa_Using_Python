class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b in a:
            return 1
        p = 1
        aL, bL = len(a), len(b)
        aS = a

        while len(aS) <= bL + aL:
            aS += a
            p += 1
            if b in aS:
                return p
        return -1
