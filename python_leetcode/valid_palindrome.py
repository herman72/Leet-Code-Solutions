# Intuition
# The problem requires checking if a string is a palindrome after ignoring non-alphanumeric characters
# and treating uppercase and lowercase letters as the same. The key insight is to first normalize
# the string by removing unwanted characters and converting to lowercase, then check if it reads
# the same forwards and backwards.

# A palindrome has the property that the character at position i equals the character at position
# (n-i-1) for all valid positions. We can leverage this by comparing characters from the start
# with their corresponding characters from the end.

# Approach
# We use a two-step approach:
# 1. **Preprocessing:** Create a cleaned version of the string by:
#    - Filtering out all non-alphanumeric characters using isalnum()
#    - Converting all characters to lowercase for case-insensitive comparison
# 2. **Palindrome Check:** Iterate through the cleaned string:
#    - For each position i, compare clean[i] with clean[len(clean)-i-1]
#    - If any pair doesn't match, immediately return False
#    - If all pairs match, return True

# This approach ensures we only process valid characters and handles the comparison efficiently
# by checking from both ends simultaneously.

# Complexity
# - **Time complexity:**
#   The preprocessing step iterates through all n characters to filter and convert them: O(n).
#   The palindrome check iterates through at most n/2 positions: O(n).
#   Overall time complexity is **O(n)**, where n is the length of the input string.

# - **Space complexity:**
#   We create a new string 'clean' that stores only alphanumeric characters from the input.
#   In the worst case (all characters are alphanumeric), this requires O(n) space.
#   Therefore, the space complexity is **O(n)**.

class Solution:
    def is_palindrome(self, s: str) -> bool:
        clean = "".join(char for char in s if char.isalnum()).lower()
        
        for i in range(len(clean)):
            if clean[i] != clean[len(clean)-i-1]:
                return False
        
        return True

if __name__=="__main__":
    # s = "A man, a plan, a canal: Panama"
    # s = "race a car"
    s ="0P"
    print(Solution().is_palindrome(s=s))