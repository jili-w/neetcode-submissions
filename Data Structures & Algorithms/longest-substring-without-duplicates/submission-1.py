class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        best = 0
        start = 0
        for i, p in enumerate(s):
            if p in seen and seen[p] >= start:
                start = seen[p] + 1
        
            seen[p] = i
            best = max(i-start + 1, best)
        return best