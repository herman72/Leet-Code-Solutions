from typing import List

# Intuition
# The problem requires finding two numbers in a sorted array that add up to a target value.
# The key insight is to leverage the fact that the array is already sorted in non-decreasing order.
# This sorting property allows us to use a two-pointer technique that eliminates the need for
# nested loops or hash maps.

# When we place one pointer at the start and another at the end, we can make intelligent decisions:
# if the sum is too large, we move the right pointer left to decrease the sum; if the sum is too
# small, we move the left pointer right to increase the sum. This converging approach efficiently
# narrows down to the solution.

# Approach 1: Two-Pointer (Optimal)
# We use a two-pointer technique that takes advantage of the sorted array:
# 1. Initialize `left` pointer at index 0 (smallest element)
# 2. Initialize `right` pointer at index len(numbers)-1 (largest element)
# 3. While left < right:
#    - Calculate current_sum = numbers[left] + numbers[right]
#    - If current_sum equals target, return [left+1, right+1] (1-indexed)
#    - If current_sum > target, decrement right (need a smaller sum)
#    - If current_sum < target, increment left (need a larger sum)
# 4. Return empty list if no solution found (though problem guarantees exactly one solution)

# This approach works because:
# - Moving right pointer left decreases the sum (array is sorted)
# - Moving left pointer right increases the sum (array is sorted)
# - We explore all possible pairs without missing the solution

# Approach 2: Brute Force
# Check all possible pairs using nested loops:
# 1. For each element at index i from 0 to len(numbers)-2
# 2. For each element at index j from i+1 to len(numbers)-1
# 3. If numbers[i] + numbers[j] equals target, return [i+1, j+1]
# This approach is simple but inefficient for large arrays.

# Complexity
# **Two-Pointer Approach:**
# - **Time complexity:**
#   Each pointer moves at most n times (where n is the length of the array). In the worst case,
#   the pointers meet after scanning through the entire array once. Therefore, **O(n)**.

# - **Space complexity:**
#   We only use two integer pointers (left, right) and one variable for current_sum.
#   Therefore, **O(1)** constant extra space.

# **Brute Force Approach:**
# - **Time complexity:**
#   The outer loop runs n-1 times, and for each iteration, the inner loop runs up to n-1 times.
#   This results in checking approximately n²/2 pairs. Therefore, **O(n²)**.

# - **Space complexity:**
#   Only uses loop variables and no additional data structures. Therefore, **O(1)**.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two-Pointer Approach (Optimal for sorted array)
        left, right = 0, len(numbers)-1
        while left<right:
            
            current_sum = numbers[left] + numbers[right]
            if target == current_sum:
                return [left+1, right+1]
            if current_sum > target:
                right -=1
            else:
                left +=1
        return []
    
    # def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
    #     # Brute Force Approach (Less efficient but straightforward)
    #     for i in range(len(numbers)-1):
    #         for j in range(i+1, len(numbers)):
    #             if numbers[i] + numbers[j] == target:
    #                 return [i+1, j+1]
    #     return []
        