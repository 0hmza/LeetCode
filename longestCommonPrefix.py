class Solution:
    def longestCommonPrefix(self, v: List[str]) -> str:
        commonprefix = ""
        v = sorted(v)
        first_str = v[0]
        last_str = v[-1]
        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] != last_str[i]:
                return commonprefix
            commonprefix += first_str[i]
        return commonprefix