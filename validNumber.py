class Solution:
    def isNumber(self, s: str) -> bool:
        i = 0
        if '.' in s or 'e' in s or 'E' in s:
            try:
                float(s)
                return True
            except Exception:
                return False
        else:
            try:
                int(s)
                return True
            except Exception:
                return False
        return False


answer = Solution()
print(answer.isNumber("95a54e53"))
print(float("-0.1"))