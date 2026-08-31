class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_ct = {}
        for ch in s:
            char_ct[ch] = char_ct.get(ch, 0) + 1

        for ch in t:
            if ch not in char_ct:
                return False
            if char_ct[ch] == 0:
                return False
            char_ct[ch] -= 1

        return True