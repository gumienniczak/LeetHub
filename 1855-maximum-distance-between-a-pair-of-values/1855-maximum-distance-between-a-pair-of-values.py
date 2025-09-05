class Solution(object):
    def maxDistance(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        max_dist = 0
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if i <= j and nums1[i] <= nums2[j]:
                max_dist = max(max_dist, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
        
        return max_dist