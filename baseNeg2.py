class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        res = ""
        while n != 0:
            reminder = n % 2
            n = (n - reminder) // (-2)
            res += str(reminder)
        return "".join(reversed(res))


## Test ###
answer = Solution()
print(answer.baseNeg2(4))
def chek(num:int):
    digit = "01234567"
    j = 1
    n = num
    if n < 0:
        n = n * (-1)
    t = ""
    r = "-"
    while n != 0:
        t += digit[n % 7]
        n //= 7
    if num < 0:
        r += "".join(reversed(t))
        return r
    else:
        return "".join(reversed(t))
print(chek(7))
