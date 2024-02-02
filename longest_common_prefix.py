class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        firstStr = strs[0]
        result = ""
        for i in range(0, len(firstStr)):
            for s in strs:
                if  i == len(s) or s[i] != firstStr[i]:
                    return result
            result += firstStr[i]
        return result