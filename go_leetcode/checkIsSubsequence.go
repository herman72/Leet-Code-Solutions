package main

// # Intuition
// The problem requires checking whether the string `s` appears as a subsequence in string `t`. A subsequence means the characters of `s` appear in `t` in the same order, but not necessarily consecutively. 

// The idea is to iterate through `t` while keeping track of how many characters of `s` have been matched so far. If all characters in `s` are found in `t` in order, then `s` is a subsequence of `t`.

// # Approach
// We use a two-pointer approach:
// 1. Initialize a pointer `k` to track the position in `s`.
// 2. Iterate over each character of `t`:
//    - If the current character in `t` matches the character at index `k` in `s`, move `k` forward.
//    - If `k` reaches the length of `s`, it means all characters of `s` have been found in order, so return `true`.
// 3. If the loop completes without `k` reaching the end of `s`, return `false`.

// This approach efficiently scans through `t` while making a single pass over `s`.

// # Complexity
// - **Time complexity:**  
//   The function iterates through `t` once, and in the worst case, checks every character of `t` against `s`. Thus, the time complexity is **$$O(n)$$**, where `n` is the length of `t`.

// - **Space complexity:**  
//   The function uses only a few integer variables (`k` and loop iterators), so it operates in **$$O(1)$$** space.

// # Code

// func main(){
// 	s := " "
// 	fmt.Println(isPalindrome(s))

// }


func isSubsequence(s, t string) bool {
    k := 0
    for _, char := range t {
        if k < len(s) && char == rune(s[k]) {
            k++
        }
        if k == len(s) {
            return true
        }
    }
    return k == len(s)
}
