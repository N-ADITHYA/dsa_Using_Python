class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        char = ""
        for c in s:
            if c != "-":
                char += c.upper()
        n = len(char)
        rem = n % k
        if rem == 0:
            rem = k

        ans = char[:rem]
        i = rem

        while i < n:
            ans += "-"
            ans += char[i:i + k]
            i += k
        return ans
