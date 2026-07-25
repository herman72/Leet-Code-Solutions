from collections import Counter

# Intuition
# Two strings are anagrams when they contain exactly the same
# characters with exactly the same frequencies, only in a
# different order. The key insight is that order is the one
# thing we are allowed to ignore, so any solution boils down
# to reducing both strings to an order-independent form and
# comparing those forms.

# There are two natural ways to erase order. The first is to
# impose a canonical order on both strings by sorting them:
# if they are anagrams, the sorted results are identical. The
# second is to never look at order at all and instead count
# how many times each character appears; if every count
# matches, the strings are anagrams. Counting is cheaper
# because it visits each character once instead of paying for
# a comparison sort.

# A useful early exit for every counting variant: if the two
# strings have different lengths they cannot be anagrams, so
# we can return False before doing any work.

# Approach 1: Sorting
# 1. Sort the characters of s and the characters of t
# 2. Compare the two sorted sequences for equality
# Simple and short, but pays the cost of a comparison sort.

# Approach 2: Counter (Optimal, idiomatic)
# 1. Build a frequency map of s with collections.Counter
# 2. Build a frequency map of t the same way
# 3. Compare the two maps for equality
# Counter equality already handles differing lengths and
# characters present in one string but not the other.

# Approach 3: Hash Map Counting (Optimal, explicit)
# The same idea as Approach 2, written out by hand:
# 1. If len(s) != len(t), return False
# 2. Walk s and increment counts[ch] for each character
# 3. Walk t and for each character:
#    - If ch is not in counts, return False (t has a
#      character s never had, or too many of it)
#    - Decrement counts[ch], and delete the key when it
#      reaches 0
# 4. Return True if the map is now empty
# Because the lengths are equal, an empty map at the end
# means every character was matched exactly.

# Approach 4: Fixed 26-Slot Array (Optimal, fastest constant)
# Valid only when the input is guaranteed lowercase a-z:
# 1. If len(s) != len(t), return False
# 2. Allocate counts = [0] * 26
# 3. Walk both strings in lockstep, incrementing the slot for
#    the character from s and decrementing the slot for the
#    character from t
# 4. Return True if every slot is back to 0
# Array indexing avoids hashing entirely, so this is the
# fastest in practice despite the same asymptotic bound.

# Complexity
# **Sorting Approach:**
# - **Time complexity:**
#   Sorting each string dominates the work, and comparing the
#   two sorted sequences is linear. Therefore, **O(n log n)**.

# - **Space complexity:**
#   sorted() builds a new list of characters for each string.
#   Therefore, **O(n)**.

# **Counter / Hash Map Approach:**
# - **Time complexity:**
#   Each string is scanned once and every map operation is
#   O(1) on average. Therefore, **O(n)**.

# - **Space complexity:**
#   The map holds at most one key per distinct character. For
#   a fixed alphabet this is bounded by a constant, so
#   **O(1)** (or **O(k)** for an alphabet of size k).

# **Fixed Array Approach:**
# - **Time complexity:**
#   One pass over both strings plus a fixed 26-slot check.
#   Therefore, **O(n)**.

# - **Space complexity:**
#   The counts array is always exactly 26 entries regardless
#   of input size. Therefore, **O(1)**.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """Sorting: O(n log n) time, O(n) space."""
        return sorted(s) == sorted(t)

    def isAnagramCounter(self, s: str, t: str) -> bool:
        """Counter: O(n) time, O(1) space (at most 26 keys)."""
        return Counter(s) == Counter(t)

    def isAnagramHashMap(self, s: str, t: str) -> bool:
        """Manual counting: O(n) time, O(1) space."""
        if len(s) != len(t):
            return False

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]

        return not counts

    def isAnagramArray(self, s: str, t: str) -> bool:
        """Fixed 26-slot array: O(n) time, O(1) space. Lowercase a-z only."""
        if len(s) != len(t):
            return False

        counts = [0] * 26
        for a, b in zip(s, t):
            counts[ord(a) - ord("a")] += 1
            counts[ord(b) - ord("a")] -= 1

        return all(c == 0 for c in counts)


if __name__ == '__main__':
    cases = [("rat", "car"), ("anagram", "nagaram"), ("a", "ab")]
    solution = Solution()

    for s, t in cases:
        print(
            s, t,
            solution.isAnagram(s=s, t=t),
            solution.isAnagramCounter(s=s, t=t),
            solution.isAnagramHashMap(s=s, t=t),
            solution.isAnagramArray(s=s, t=t),
        )
