# Intuition
# The problem requires checking if string `s` is a subsequence of string `t`. A subsequence means
# that all characters of `s` appear in `t` in the same order, but not necessarily consecutively.
# The key insight is that we can greedily match characters: for each character in `s`, find its
# first occurrence in the remaining portion of `t`.

# We don't need to track indices or store matches - we just need to verify that we can find all
# characters of `s` in order within `t`. This naturally leads to a two-pointer solution where
# we scan through `t` once and match characters from `s` as we find them.

# Approach
# We use a two-pointer technique:
# 1. Initialize pointer `s_idx` at 0 to track our position in string `s`
# 2. Initialize pointer `t_idx` at 0 to scan through string `t`
# 3. While both pointers are within their respective bounds:
#    - If s[s_idx] matches t[t_idx], we found a match, so increment s_idx
#    - Always increment t_idx to continue scanning through t
# 4. After scanning all of t, check if s_idx reached the end of s (all characters matched)
# 5. Return True if s_idx == len(s), meaning all characters were found in order

# This greedy approach works because finding each character at its earliest possible position
# in `t` maximizes our chances of finding subsequent characters.

# Complexity
# - **Time complexity:**
#   We scan through string `t` once with at most len(t) iterations. Each iteration does constant work.
#   Therefore, the time complexity is **O(n)**, where n is the length of string `t`.

# - **Space complexity:**
#   We only use two integer pointers (s_idx, t_idx) regardless of input size.
#   Therefore, the space complexity is **O(1)** (constant extra space).

class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        
        for t_idx in range(len(t)):
            if s_idx < len(s) and s[s_idx] == t[t_idx]:
                s_idx += 1
        
        return s_idx == len(s)

if __name__=="__main__":
    # s = "abc"
    # t = "ahbgdc"
    # s = "axc"
    # t = "ahbgdc"
    # s ="acb"
    # t ="ahbgdc"
    # s ="bb"
    # t ="ahbgdc"
    s = "aza"
    t = "abzba"
    print(Solution().is_subsequence(s=s, t=t))