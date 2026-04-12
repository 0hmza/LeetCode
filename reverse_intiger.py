class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            if -int(str(x)[:0:-1]) < -pow(2,31):
                return 0
            else:
                return -int(str(x)[:0:-1])
        else:
            if int(str(x)[::-1]) > pow(2,31) - 1:
                return 0
            else:
                return int(str(x)[::-1])