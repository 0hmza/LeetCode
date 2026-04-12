class Solution:
    def isHappy(self, n: int) -> bool:
        num = str(n)
        p = sum(pow(int(i), 2) for i in num)
        if p == 1 or p == 7 or p == 10:
            return True
        elif p > 10:
            return self.isHappy(p)
        else:
            return False
            


anwer = Solution()
print(anwer.isHappy(4))


















class Solution:
    def isHappy(self, n: int) -> bool:
        h = set()
        def hlper(num: int, t:set):
            if num == 1:
                return True
            if num in t:
                return False
            t.add(num)
            p = sum(pow(int(i), 2) for i in str(num))
            return hlper(p, t)
            
        
        return hlper(n, h)


