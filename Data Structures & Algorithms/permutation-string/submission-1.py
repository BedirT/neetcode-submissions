class Solution:
    def reset(self, hsh: dict):
        for k in hsh.keys():
            hsh[k] = 0
        return hsh

    def checkInclusion(self, s1: str, s2: str) -> bool:
        hsh = {}
        check = {} # to check the vals
        for x in s1:
            if x not in hsh:
                hsh[x] = 0
                check[x] = 0
            hsh[x] += 1
        
        counter = 0
        cur_str_init_idx = 0
        for step, char in enumerate(s2):
            if char not in hsh:
                if counter:
                    # reset
                    counter = 0
                    check = self.reset(check)
                continue

            if check[char] >= hsh[char]:
                if s2[cur_str_init_idx] == char:
                    # replace that initial char with the current one
                    cur_str_init_idx += 1
                else:
                    # reset
                    counter = 0
                    check = self.reset(check)
                continue

            # if here char in hsh and in limit
            if counter == 0:
                cur_str_init_idx = step # mark the current sbs start
            check[char] += 1
            counter += 1

            if counter == len(s1):
                # all items found
                return True

        return False
