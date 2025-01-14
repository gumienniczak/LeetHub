class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        common = len(A) * [0]
        for i in range(len(A)):
            subset_A = set(A[0:i+1])
            subset_B = set(B[0:i+1])
            common[i] = len(subset_A.intersection(subset_B))
        return common