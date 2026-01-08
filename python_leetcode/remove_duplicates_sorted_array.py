# Intuition
# The problem requires removing duplicates from a sorted array in-place, keeping only unique elements.
# Since the array is already sorted, all duplicates are adjacent to each other. This property allows
# us to use a simple linear scan to identify unique elements without needing extra space for tracking.

# The key insight is that we don't need to shift or delete elements - we only need to ensure the first
# `k` positions contain the unique elements in order. Elements beyond position `k` can be ignored.
# By comparing each element with its predecessor, we can identify when we encounter a new unique value.

# Approach
# We use a two-pointer approach:
# 1. Initialize pointer `k` at 1, which tracks the position where the next unique element should be placed
#    (We start at 1 because the first element is always unique)
# 2. Use pointer `i` to iterate through the array starting from index 1
# 3. For each element at index i:
#    - If nums[i] != nums[i-1], we've found a new unique element
#    - Place this unique element at position k: nums[k] = nums[i]
#    - Increment k to prepare for the next unique element
# 4. Return k, which represents the count of unique elements

# This approach maintains the relative order of unique elements and modifies the array in-place.

# Complexity
# - **Time complexity:**
#   We iterate through the array once with a single pass, examining each element exactly once.
#   Each comparison and assignment operation takes O(1) time. Thus, the time complexity is **O(n)**,
#   where n is the length of the array.

# - **Space complexity:**
#   The function modifies nums in-place using only a few variables (k, i) regardless of input size.
#   Therefore, the space complexity is **O(1)** - constant extra space.

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1
        
        return k

if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    k = Solution().removeDuplicates(nums)
    print(k)
    print(nums)
    

# k = [0, 4, 1, 1, 2, ]
# print(k.pop(1))
# print(k)
# k.append("_")
# print(k)