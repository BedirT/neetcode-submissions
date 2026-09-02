import re


class Solution:

    delimeter = "<br_h>"
    def encode(self, strs: List[str]) -> str: 
        if not strs:
            return self.delimeter * 2
        return self.delimeter.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == self.delimeter * 2:
            return []
        idxs = set([match.start() for match in re.finditer(self.delimeter, s)])
        d_len = len(self.delimeter)
        res = []
        
        i = 0
        last_idx = 0
        while i < len(s):
            
            if i in idxs:
                # delimeter point
                res.append(s[last_idx:i])
                i += d_len
                last_idx = i
            else:
                i += 1 
        res.append(s[last_idx:])

        return res