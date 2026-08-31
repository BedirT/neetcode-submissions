class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right, left = 0, 0
        ct = {}
        max_freq = 0
        while right < len(s):
            if s[right] not in ct:
                ct[s[right]] = 0
            ct[s[right]] += 1
            num_letters = right - left + 1
            if num_letters - max(ct.values()) <= k:
                # valid
                max_freq = max(max_freq, num_letters)
                right += 1
            else:
                ct[s[right]] -= 1 # take it back
                ct[s[left]] -= 1
                left += 1
            print(left, right, ct, max_freq)
        return max_freq
