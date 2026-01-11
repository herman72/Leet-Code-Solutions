from typing import List
class Solution:
    
    # Intuition
    # The problem requires removing duplicates from a sorted array in-place, allowing at most TWO 
    # occurrences of each unique element. Since the array is already sorted, all duplicates are 
    # adjacent to each other. This property allows us to use a simple linear scan to identify 
    # valid elements without needing extra space for tracking.

    # The key insight is that we don't need to shift or delete elements - we only need to ensure 
    # the first `k` positions contain the valid elements (at most 2 of each) in order. Elements 
    # beyond position `k` can be ignored. By comparing each element with the element at position 
    # k-2, we can determine if adding the current element would create a third duplicate.

    # Approach
    # We use a two-pointer approach:
    # 1. Handle edge case: if array has ≤2 elements, all elements are valid, return length
    # 2. Initialize pointer `k` at 2, which tracks the position where the next valid element 
    #    should be placed (first two elements are always valid since we allow 2 duplicates)
    # 3. Use pointer `i` to iterate through the array starting from index 2
    # 4. For each element at index i:
    #    - If nums[i] != nums[k-2], this element won't create a third duplicate
    #    - Place this element at position k: nums[k] = nums[i]
    #    - Increment k to prepare for the next valid element
    # 5. Return k, which represents the count of valid elements (at most 2 of each unique value)

    # This approach maintains the relative order of elements and modifies the array in-place.

    # Complexity
    # - **Time complexity:**
    #   We iterate through the array once with a single pass, examining each element exactly once.
    #   Each comparison and assignment operation takes O(1) time. Thus, the time complexity is **O(n)**,
    #   where n is the length of the array.

    # - **Space complexity:**
    #   The function modifies nums in-place using only a few variables (k, i) regardless of input size.
    #   Therefore, the space complexity is **O(1)** - constant extra space.
    
    def remove_duplicate(self, nums: List[int]) -> int:
        # Edge case: if array has 2 or fewer elements, all are valid
        if len(nums) <= 2:
            return len(nums)
        
        # First two elements are always valid (at most 2 duplicates allowed)
        k = 2
        
        # Start from the third element
        for i in range(2, len(nums)):
            # Key insight: if current element differs from element at position k-2,
            # we can include it (ensures at most 2 duplicates)
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        
        return k

if __name__ == "__main__":
    # Test case 1
    nums1 = [1,1,1,2,2,3]
    k1 = Solution().remove_duplicate(nums=nums1)
    print(f"Test 1: k = {k1}, nums = {nums1[:k1]}")
    # Expected: k = 5, nums = [1,1,2,2,3]
    
    # Test case 2
    nums2 = [0,0,1,1,1,1,2,3,3]
    k2 = Solution().remove_duplicate(nums=nums2)
    print(f"Test 2: k = {k2}, nums = {nums2[:k2]}")
    # Expected: k = 7, nums = [0,0,1,1,2,3,3]