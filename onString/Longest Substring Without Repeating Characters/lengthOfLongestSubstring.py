class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, count, r = 0, 0, 0
        ans = 0
        char_set = set()
        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                ans = max(ans, r - l + 1)
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        return ans