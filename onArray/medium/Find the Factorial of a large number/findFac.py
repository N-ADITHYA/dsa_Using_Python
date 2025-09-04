class Solution:
    def findFac(self, n: int) -> str:
        digits = [1]
        for i in range(2, n + 1):
            carry = 0
            for k in range(len(digits)):
                prod = digits[k] * i + carry
                digits[k] = prod % 10
                carry = prod // 10

            while carry > 0:
                digits.append(carry % 10)
                carry //= 10
        return "".join(map(str, digits[::-1]))
