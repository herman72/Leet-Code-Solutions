
# Intuition
# The problem requires finding the majority element - the element that appears more than n/2 times.
# The key insight is that we need to count how many times each element appears in the array.
# A dictionary (hash map) is perfect for this because it can store element-count pairs efficiently,
# regardless of whether the numbers are positive, negative, or extremely large.

# Unlike an array-based counting approach (which would fail with large numbers like 1000000000
# or negative numbers), a dictionary only creates entries for elements that actually exist in
# the input array, making it memory-efficient.

# Once we have the counts, we simply need to find which element has the highest count - that's
# our majority element.

# Approach
# We use a hash map (dictionary) counting approach:
# 1. Initialize an empty dictionary `count` to store element frequencies
# 2. Iterate through each number in the input array:
#    - Use dict.get(num, 0) to retrieve the current count (or 0 if not present)
#    - Increment the count by 1 and store it back in the dictionary
# 3. After counting all elements, use max() with a custom key function:
#    - The key function `lambda x: count[x]` tells max() to compare dictionary values (counts)
#    - max() returns the dictionary key (the number) that has the highest count
# 4. Return this element as the majority element

# This approach works for any integer values and handles edge cases like negative numbers
# and extremely large values without memory issues.

# Complexity
# - **Time complexity:**
#   We iterate through the array once to build the count dictionary: O(n)
#   Finding the max element involves iterating through the unique elements: O(k) where k is unique elements
#   Since k ≤ n, the overall time complexity is **O(n)**

# - **Space complexity:**
#   The dictionary stores at most n entries (if all elements are unique)
#   Therefore, space complexity is **O(n)** in the worst case, or **O(k)** where k is the number of unique elements
from typing import List

class Solution:
    def majority_element(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return max(count, key=lambda x: count[x])
        
if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(Solution().majority_element(nums=nums))