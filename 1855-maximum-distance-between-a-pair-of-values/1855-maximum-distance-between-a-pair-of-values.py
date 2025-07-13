class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums1)):
            left = i
            right = len(nums2) - 1
            while left <= right:
                mid = (right + left) // 2
                if nums1[i] <= nums2[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        
            ans = max(ans, right - i)
        
        return ans