class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        from math import factorial as f
        h = {}
        for i, n in enumerate(nums):
            h[n] = h.get(n, 0) + 1
        
        num_pairs = 0
        for k, v in h.items():
            num_pairs += f(v) // (f(2) * f(max(0, v - 2)))
        return num_pairs