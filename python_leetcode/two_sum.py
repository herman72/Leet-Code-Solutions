from typing import List

# Intuition
# We need two different positions i and j where
# nums[i] + nums[j] == target. For each number x, the partner
# we need is fixed: target - x (the complement). So the real
# question is: "Have I seen the complement of x before?"

# The brute force answers that question by scanning every
# other number. A hash map answers it in O(1), because it can
# look up a value and return its index directly. This is the
# classic trade: spend O(n) memory to remove one nested loop.

# Approach 1: Brute Force (this solution)
# 1. For every i, loop over every j > i
# 2. If nums[i] + nums[j] == target, return [i, j]
# 3. If no pair is found, return []
# Easy to get right, and it uses no extra memory. But it is
# too slow for large inputs.

# Approach 2: One-Pass Hash Map (Optimal)
# 1. Keep a map seen: value -> index
# 2. For each index i and value x, compute need = target - x
# 3. If need is in seen, return [seen[need], i]
# 4. Otherwise store seen[x] = i and continue
# We check the map BEFORE we store x. This stops a number from
# pairing with itself, and it still works for duplicates
# (for example [5, 5] with target 10).

# Why not sort and use two pointers?
# Sorting gives O(n log n) time, and it destroys the original
# indices. We would have to store (value, index) pairs first.
# It is a good fit when the array is already sorted (see
# two_sum_two.py), but it is not the best choice here.

# Complexity
# **Brute Force Approach:**
# - **Time complexity:**
#   For each i we scan up to n - i - 1 numbers, which is about
#   n^2 / 2 checks in total. Therefore, **O(n^2)**.

# - **Space complexity:**
#   Only loop counters are used. Therefore, **O(1)**.

# **Hash Map Approach:**
# - **Time complexity:**
#   One pass, and each lookup and insert is O(1) on average.
#   Therefore, **O(n)**.

# - **Space complexity:**
#   In the worst case the map stores every number.
#   Therefore, **O(n)**.


class Solution:
    def twoSum(self, nums: List[int], targets: int) -> List[int]:
        """Brute force: O(n^2) time, O(1) space."""
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == targets:
                    return [i, j]
        return []

    def twoSumHashMap(self, nums: List[int], targets: int) -> List[int]:
        """One-pass hash map: O(n) time, O(n) space."""
        seen = {}
        for i, x in enumerate(nums):
            need = targets - x
            if need in seen:
                return [seen[need], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    cases = [
        ([3, 4, 5, 6], 7),
        ([4, 5, 6], 10),
        ([5, 5], 10),
        ([-1, -2, -3, -4, -5], -8),
    ]
    solution = Solution()

    for nums, target in cases:
        print(
            nums, target,
            solution.twoSum(nums=nums, targets=target),
            solution.twoSumHashMap(nums=nums, targets=target),
        )

