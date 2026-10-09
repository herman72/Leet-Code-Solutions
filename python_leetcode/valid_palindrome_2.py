import re

# Intuition
# A phrase is a palindrome when it reads the same forward and
# backward after we ignore everything that is not a letter or
# a digit, and ignore letter case. The problem has two parts:
# (1) decide which characters count, and (2) compare the
# string with its mirror image.

# Part (2) only needs half of the work. Character i must match
# character n - 1 - i. When we check the first half, the second
# half is already covered by symmetry, so checking all n
# positions repeats every comparison twice.

# Approach 1: Regex Clean + Index Compare (this solution)
# 1. Remove every non-alphanumeric character with a regex
# 2. Convert the result to lowercase
# 3. Compare s[i] with s[n - 1 - i] for every i
# Correct, but it has three weak points:
# - re.compile runs on every call (the re module caches
#   patterns, but a module-level constant is cleaner)
# - It builds two new strings before the first comparison
# - The loop runs n times, but n // 2 is enough

# Approach 2: Clean + Reverse (Short, idiomatic)
# 1. Keep only characters where ch.isalnum() is True, in
#    lowercase
# 2. Return cleaned == cleaned[::-1]
# Shortest code. Still uses O(n) extra space.

# Approach 3: Two Pointers (Optimal, recommended)
# 1. Put left at the start and right at the end
# 2. If s[left] is not alphanumeric, move left forward
# 3. If s[right] is not alphanumeric, move right backward
# 4. If the two lowercase characters are different, return
#    False
# 5. Move both pointers inward and repeat while left < right
# 6. Return True
# No new string is built, and it stops at the first mismatch.
# It also handles the empty string and " " (return True).

# Complexity
# **Regex / Reverse Approach:**
# - **Time complexity:**
#   One pass to clean the string and one pass to compare.
#   Therefore, **O(n)**.

# - **Space complexity:**
#   The cleaned string (and its reverse) is a new copy of the
#   input. Therefore, **O(n)**.

# **Two Pointers Approach:**
# - **Time complexity:**
#   Each pointer moves across the string at most once.
#   Therefore, **O(n)**.

# - **Space complexity:**
#   Only two integer pointers are used. Therefore, **O(1)**.

# Note: str.isalnum() accepts Unicode letters and digits, but
# the regex [^a-zA-Z0-9] accepts ASCII only. LeetCode inputs
# are ASCII, so both give the same result here.


class Solution:
    def isPalindorm(self, s: str) -> bool:
        """Regex clean + index compare: O(n) time, O(n) space."""
        regex = re.compile('[^a-zA-Z0-9]')
        s = regex.sub('', s)
        s = s.lower()
        for i in range(len(s)):
            if s[i] != s[len(s) - i -1]:
                return False
        
        return True

    def isPalindromeReverse(self, s: str) -> bool:
        """Clean + reverse: O(n) time, O(n) space."""
        cleaned = [ch.lower() for ch in s if ch.isalnum()]
        return cleaned == cleaned[::-1]

    def isPalindromeTwoPointers(self, s: str) -> bool:
        """Two pointers: O(n) time, O(1) space."""
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1

        return True
        
if __name__ == '__main__':
    solution = Solution()
    cases = ["Was it a car or a cat I saw?", "race a car", " ", "0P"]

    for s in cases:
        print(
            repr(s),
            solution.isPalindorm(s=s),
            solution.isPalindromeReverse(s=s),
            solution.isPalindromeTwoPointers(s=s),
        )
        