class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        u = {}
        m = {}
        if len(s) != len(t):
            return False

        for ltr in s:
            u[ltr] = u.get(ltr,0) + 1
        for ltr in t:
            m[ltr] = m.get(ltr,0) + 1
        
        return u == m

                
