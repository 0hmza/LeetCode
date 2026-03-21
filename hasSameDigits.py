class Solution:
    def hasSameDigits(self, s: str) -> bool:
        d = ""
        i = 0
        while i < len(s) - 1:
            d += str((int(int(s[i]) + int(s[i+ 1])) % 10))
            i += 1
        if len(d) == 2:
            if d[0] == d[1]:
                return True
            return False
        return self.hasSameDigits(d)






answer = Solution()
print(answer.hasSameDigits("3902"))