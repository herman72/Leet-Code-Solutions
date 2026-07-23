# Intuition
# The problem requires determining if any value appears at
# least twice in the array. The key insight is that we need
# to efficiently track which elements we've already seen.
# A set is ideal for this because it provides O(1) average
# lookup and insertion, and automatically handles any integer
# values (positive, negative, or very large).

# As we iterate through the array, we check if the current
# element already exists in our set. If it does, we've found
# a duplicate and can return immediately. If we finish
# scanning without finding any duplicates, the array contains
# all unique elements.

# Approach
# We use a hash set to track seen elements:
# 1. Initialize an empty set `seen`
# 2. Iterate through each number in the array:
#    - If the number is already in `seen`, return True
#      (duplicate found)
#    - Otherwise, add the number to `seen`
# 3. If we finish the loop without finding duplicates,
#    return False

# This approach returns early on the first duplicate found,
# making it efficient for arrays where duplicates appear
# early.

# Complexity
# - **Time complexity:**
#   We iterate through the array once. Each set lookup and
#   insertion is O(1) on average. Therefore, the time
#   complexity is **O(n)**, where n is the length of the
#   array.

# - **Space complexity:**
#   In the worst case (all unique elements), the set stores
#   n elements. Therefore, the space complexity is **O(n)**.

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        # or return len(nums) != len(set(nums)) which is less efficient but more concise
        # Because it always processes the entire array — it builds a full set from all
        # elements before comparing lengths. There's no short-circuiting.

        # With the loop approach, if nums = [1, 1, 2, 3, ..., 1_000_000], it returns
        # True after just 2 iterations (when it sees the second 1).

        # With len(nums) != len(set(nums)), it converts all 1,000,000 elements into a
        # set first, then compares — doing ~999,998 unnecessary operations.

        # Same worst-case (all unique): both are O(n). Best/average case: the loop is
        # faster when duplicates exist early.


if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    nums2 = [1, 2, 3, 4]
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    nums4 = [3, 3]
    print(Solution().containsDuplicate(nums=nums1))
    print(Solution().containsDuplicate(nums=nums2))
    print(Solution().containsDuplicate(nums=nums3))
    print(Solution().containsDuplicate(nums=nums4))
