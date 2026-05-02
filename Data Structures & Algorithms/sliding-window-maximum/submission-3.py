class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n  = len(nums)
        left_max = [0] * n
        right_max = [0] *n

        left_max[0] = nums[0]
        right_max[n-1] = nums[n-1]

        for i in range(n):
            if i%k == 0:
                left_max[i] = nums[i]
            else:
                left_max[i] = max(left_max[i-1],nums[i])
            
            j = n-1-i
            if (j+1)%k == 0 or j == n -1:
                right_max[j] = nums[j]
            else:
                right_max[j] = max(right_max[j+1],nums[j])
        result = [0]*(n-k+1)

        for i in range(n-k+1):
            result[i] = max(left_max[i+k-1],right_max[i])

        return result

        