class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1
                count = max(count, curr_count)
            else:
                curr_count = 0

        
        return count