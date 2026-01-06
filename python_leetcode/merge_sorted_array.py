# Intuition
# The problem requires merging two sorted arrays nums1 and nums2 into nums1 in-place.
# The key insight is that nums1 has enough space at the end to hold all elements from both arrays.
# Since both arrays are already sorted, we can avoid using extra space by filling nums1 from
# the back (right to left) rather than from the front. This prevents overwriting elements we
# haven't processed yet.

# By comparing the largest unmerged elements from both arrays and placing the larger one at
# the rightmost available position, we naturally maintain sorted order while working backwards.

# Approach
# We use a three-pointer approach working backwards:
# 1. Initialize pointer `j` at the last valid element of nums1 (index m-1)
# 2. Initialize pointer `k` at the last element of nums2 (index n-1)
# 3. Initialize pointer `i` at the last position of the merged array (index m+n-1)
# 4. Iterate backwards from i = m+n-1 to 0:
#    - If k < 0, all nums2 elements are placed, remaining nums1 elements are already in position, break
#    - If j >= 0 and nums1[j] > nums2[k], place nums1[j] at position i and decrement j
#    - Otherwise, place nums2[k] at position i and decrement k
# 5. This ensures the largest remaining element is always placed at the current position

# This approach efficiently merges in a single pass without needing extra space for a temporary array.

# Complexity
# - **Time complexity:**
#   The function iterates through at most m+n positions once, comparing and placing elements.
#   Thus, the time complexity is **O(m + n)**, where m and n are the lengths of the two arrays.

# - **Space complexity:**
#   The function modifies nums1 in-place using only a few pointer variables (i, j, k).
#   Therefore, it operates in **O(1)** space (constant extra space).

from typing import List


class Solution:
    def merge(self, nums1: List[int], nums2: List[int], m: int, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = m - 1
        k = n - 1
        for i in range(m + n - 1, -1, -1):
            if k < 0:
                break
            if j >= 0 and nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1


if __name__ == "__main__":
    # nums1 = [1,2,3,0,0,0]
    # m = 3
    # nums2 = [2,5,6]
    # n = 3
    test_nums1 = [1]
    test_m = 1
    test_nums2 = []
    test_n = 0
    Solution().merge(test_nums1, test_nums2, test_m, test_n)
    print(test_nums1)  # Output should be [1,2,2,3,5,6]