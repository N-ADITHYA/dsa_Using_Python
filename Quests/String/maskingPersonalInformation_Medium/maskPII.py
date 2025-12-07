class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s:
            i = 0
            ans = ""
            ast = "*" * 5

            while i < len(s):
                if s[i] == "@":
                    ans += s[0].lower() + ast + s[i - 1].lower()
                    break
                i += 1
            ans += s[i:].lower()
        else:
            number = ""
            ans = ""
            sett = {'+', '-', '(', ')', ' '}
            for i in range(len(s)):
                if s[i] not in sett:
                    number += s[i]
            diff = len(number) - 10
            template = ("*" * 3) + "-" + ("*" * 3) + "-" + number[6 + diff:len(number)]
            if diff == 0:
                ans += template
            elif diff == 1:
                ans += ("+*" + "-") + template
            elif diff == 2:
                ans += ("+**" + "-") + template
            else:
                ans += ("+***" + "-") + template
        return ans

