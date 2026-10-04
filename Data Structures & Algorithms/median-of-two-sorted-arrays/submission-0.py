class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n1,n2 = nums1,nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(n2) < len(n1):
            n1,n2 = n2,n1
        
        left, right = 0, len(n1) -1
        while True:
            i = (left + right )//2
            j = half - i -2
            n1_left = n1[i] if i>=0 else float("-infinity")
            n1_right = n1[i+1] if (i+1) < len(n1) else float("infinity")
            n2_left = n2[j] if j >= 0 else float("-infinity")
            n2_right = n2[j+1] if (j+1) < len(n2) else float("infinity")

            if n1_left <= n2_right and n2_left <= n1_right:
                if total % 2:
                    return min(n1_right,n2_right)
                return (max(n1_left,n2_left) + min(n1_right,n2_right))/2
            elif n1_left > n2_right:
                right = i-1
            else:  
                left = i +1
