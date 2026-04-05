class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        r = 0 
        t = 1

        while i < len(s) and s[i].isspace():
            i += 1

        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                t = t * (-1)
            i += 1

        while i < len(s) and (chr(48) <=s[i] <= chr(57)):
            r = r * 10 + int(s[i])
            i += 1
        if r * t <= -pow(2, 31):
            return -pow(2, 31)
        elif r >= pow(2, 31):
            return pow(2, 31) - 1
        return r * t


answer = Solution()
print(answer.myAtoi("2147483648"))
