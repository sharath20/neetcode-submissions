class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        hash_map = {}
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        for ch in t:
            if ch in hash_map:
                hash_map[ch] -= 1
                if hash_map[ch] == 0:
                    del hash_map[ch]
        
        return True if not hash_map else False