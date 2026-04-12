class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        thislist = [i for i in range(1, n + 1)][::-1]
        p = []
        res = ""
        i = 0
        while i < len(thislist):
            j = i
            while j < len(thislist):
                temp = thislist[i]
                thislist[i] = thislist[j]
                thislist[j] = temp
                for k in thislist:
                    res += str(k)
                if res not in p:
                    p.append(res)
                res = ""
                j += 1
            i += 1
        return p[::-1]
        
answer = Solution()
print(answer.getPermutation(3, 3))