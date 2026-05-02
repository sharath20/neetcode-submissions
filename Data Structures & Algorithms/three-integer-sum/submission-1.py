class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        n = len(nums)
        for i in range(n-2):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            val = -nums[i]
            left = i+1
            right = n-1
            while left < right :
                if nums[left] + nums[right] > val:
                    right -= 1
                elif nums[left] + nums[right] < val:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    
                    while left <right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
        return res
        