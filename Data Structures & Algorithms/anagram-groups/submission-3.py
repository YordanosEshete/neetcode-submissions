from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        u = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            u[sorted_word].append(word)
    
        return list(u.values())

                