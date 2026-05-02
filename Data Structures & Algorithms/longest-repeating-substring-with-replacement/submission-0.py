class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        res = 0
        count_f = {}
        left,max_frequency = 0,0

        for right in range(len(s)):
            count_f[s[right]] = 1 + count_f.get(s[right], 0)
            max_frequency = max(max_frequency,count_f[s[right]])

            while(right-left+1)-max_frequency > k:
                count_f[s[left]] -= 1
                left += 1

            res = max(res,right-left+1) 
        
        return res