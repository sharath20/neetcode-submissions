class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for i in nums:
            if i not in result:
                result.add(i)
            else:
                return True

        return False 
         