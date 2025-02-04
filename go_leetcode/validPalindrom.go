package main

import (
	"unicode"
)

// func main(){
// 	s := " "
// 	fmt.Println(isPalindrome(s))

// }

// func isPalindrome(s string) bool {

//     var cleanString []byte

//     for _,char := range(s){
//         if unicode.IsDigit(char) || unicode.IsLetter(char){
// 			cleanString = append(cleanString, byte(unicode.ToLower(char)))
// 		}
		
// 	}

// 	for i := range cleanString {
// 		if cleanString[i] != cleanString[len(cleanString)-i-1]{
// 			return false
// 		} 
// 	}
// 	fmt.Printf("%T\n", cleanString)

// 	return true



    
// }


func isPalindrome(s string) bool {
	left, right := 0, len(s)-1

	for left < right {
		// Move left pointer to the next alphanumeric character
		for left < right && !isAlphanumeric(rune(s[left])) {
			left++
		}
		// Move right pointer to the previous alphanumeric character
		for left < right && !isAlphanumeric(rune(s[right])) {
			right--
		}

		// Compare lowercase versions of the characters
		if unicode.ToLower(rune(s[left])) != unicode.ToLower(rune(s[right])) {
			return false
		}

		left++
		right--
	}

	return true
}

// Helper function to check if a character is alphanumeric
func isAlphanumeric(ch rune) bool {
	return unicode.IsLetter(ch) || unicode.IsDigit(ch)
}