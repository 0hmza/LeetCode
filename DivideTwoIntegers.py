class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend <= -pow(2, 31) and divisor < 0:
            k = int(dividend/divisor)
            if k >= pow(2, 31):
                return pow(2, 31) - 1
        return int(dividend/divisor)