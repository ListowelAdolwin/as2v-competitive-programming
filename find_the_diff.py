class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        for i in range(len(t)):
            if i >= len(s) or s[i] != t[i]:
                return t[i]