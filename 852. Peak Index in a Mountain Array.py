from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A)):
            if A[i+1] < A[i]:
                return i


x = Solution()
print(x.peakIndexInMountainArray([0, 1, 2, 1, 0]))
# print(peakIndexInMountainArray([0, 1, 2, 1, 0]))
