from collections import Counter


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for s in strs:
            s_anagram = "".join(sorted(s))
            # print(s, s_anagram)
            anagrams[s_anagram] = anagrams.get(s_anagram, []) + [s]

        return list(anagrams.values())
