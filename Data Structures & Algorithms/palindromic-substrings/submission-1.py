class Solution:
    def countSubstrings(self, s: str) -> int:
        ct = 1 # inital for the skipped last item in loop below
        cur_str = ""

        def is_palindrome(some_str):
            return some_str == some_str[::-1]

        for i, ch in enumerate(s[:-1]):
            cur_str = ch
            ct += 1 # single letter always palindrome
            for ch2 in s[i+1:]:
                cur_str += ch2
                if is_palindrome(cur_str):
                    ct += 1
        return ct