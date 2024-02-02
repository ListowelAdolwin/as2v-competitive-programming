class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n == 1:
            return 2
        for i in range(min(n, 2), n * 2 + 1, 2):
            if i % n == 0:
                return i