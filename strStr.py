class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = ""
        i = 0
        while i <= len(haystack) - len(needle):
            s=""
            j = 0
            while j < len(needle):
                if haystack[i + j] == needle[j]:
                    s += haystack[i + j]
                else:
                    break
                j+= 1
            if s == needle:
                return i
            i+= 1
        return -1
answer = Solution()
print(answer.strStr("sadbutsad","sad"))
print(answer.strStr("leetcode","leeto" ))
print(answer.strStr("hello", "ll"))