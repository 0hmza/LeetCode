class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        thislist = []
        res = ""
        while i < len(s):
            if s[i] not in "*+/-":
                res += str(s[i])
            elif s[i] == ' ':
                i += 1
            else:
                thislist.append(int(res))
                thislist.append(s[i])
                res = ""
            i += 1
        thislist.append(int(res))
        j = 0
        new_list = []
        while j < len(thislist):
            if thislist[j] == '*':
                new_list.append(thislist[j-1] * thislist[j+1])
            elif thislist[j] == '/':
                new_list.append(thislist[j-1] // thislist[j +1])
                
            j += 1
        return new_list


answer = Solution()
print(answer.calculate("31+2*4/4"))