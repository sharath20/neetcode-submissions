class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        charCount = {}

        for i in s:
            charCount[i] = charCount.get(i,0) +1
        for j in t:
            charCount[j] = charCount.get(j,0) -1

        for k in charCount.values():
            if k != 0:
                return False
        
        return True
