ast = "*" * 5

s = "Z@Y.Z"
i = 0
ans = ""

while i < len(s):
    if s[i] == "@":
        ans += s[0].lower() + ast + s[i-1].lower()
        break
    i += 1
ans += s[i:].lower()

s = "994402627)01(+2"
sett = {'+', '-', '(', ')', ' '}
number = ""
ans = ""
for i in range(len(s)):
    if s[i] not in sett:
        number += s[i]
print(len(number))
diff = len(number) - 10
template = ("*" * 3) + "-" + ("*" * 3) + "-" + number[6+diff:len(number)]
if diff == 0:
    ans += template
elif diff == 1:
    ans += ("+*" + "-") + template
elif diff == 2:
    ans += ("+**" + "-") + template
else:
    ans += ("+***" + "-") + template
print(ans)