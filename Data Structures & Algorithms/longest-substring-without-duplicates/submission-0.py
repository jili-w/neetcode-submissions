class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        best = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                start = max(seen[s[r]]+ 1 , start)
            seen[s[r]] = r
            best = max(best , r - start +1)
        return best
            