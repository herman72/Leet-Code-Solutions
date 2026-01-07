# Intuition
# The problem requires removing all occurrences of a given value `val` from the array `nums` in-place.
# The key insight is that the order of elements beyond the first `k` elements (where `k` is the count
# of elements not equal to `val`) doesn't matter. This allows us to use a swap-with-end strategy.

# Instead of shifting elements left every time we find a match (which would be O(n²)), we can simply
# swap the matching element with the last unprocessed element and shrink the boundary of valid elements.
# This way, we avoid expensive shift operations and handle removals efficiently.

# Approach
# We use a two-pointer approach with a shrinking boundary:
# 1. Initialize pointer `i` at 0 to scan through the array
# 2. Initialize `n` to track the boundary of valid (unprocessed) elements, starting at len(nums)
# 3. While i < n:
#    - If nums[i] == val, swap it with the last valid element at nums[n-1] and decrement n
#      (Don't increment i because the swapped element needs to be checked)
#    - Otherwise, increment i to move to the next element
# 4. Return n, which represents the count of elements not equal to val

# This approach processes each element at most once, efficiently removing all matching values.

# Complexity
# - **Time complexity:**
#   In the worst case, each element is examined once. Even when swapping, we don't re-examine
#   the same position more than necessary. Thus, the time complexity is **O(n)**, where n is the
#   length of the array.

# - **Space complexity:**
#   The function modifies nums in-place using only a few pointer variables (i, n).
#   Therefore, it operates in **O(1)** space (constant extra space).

from typing import List


class Solution:
    def remove_element(self, nums: List[int], val: int) -> int:
        """
        Remove all occurrences of val in nums in-place.
        Returns the number of elements not equal to val.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                nums[i] = nums[n - 1]
                n -= 1  # Shrink the valid portion
            else:
                i += 1
        return n
        
                
if __name__ == "__main__":
    # nums_test = [3,2,2,3]
    # val_tes = 3
    
    nums_test = [0,1,2,2,3,0,4,2]
    val_test = 2
    
    k = Solution().remove_element(nums=nums_test, val=val_test)
    print(k)
    
            
            
        