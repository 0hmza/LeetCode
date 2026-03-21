class Solution:
    def isValid(self, s: str) -> bool:
        i=0
        thislist=[]
        for i in range(len(s)):
            if s[i]=='('or s[i]=='['or s[i]=='{':
                thislist.append(s[i])
            else:
                if not thislist:
                    return False
                top=thislist.pop()
                if s[i]==')'and top!='(':
                    return False
                if s[i]==']'and top!='[':
                    return False
                if s[i]=='}'and top!='{':
                    return False
        return len(thislist)==0

            
answer = Solution()
print(answer.isValid("{[]}}{}"))