# Problem: 3517. Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Link: https://leetcode.com/problems/smallest-palindromic-rearrangement-i/description

# Time Complexity: O(N) - Counting frequencies takes O(N) time. Sorting the unique characters takes O(1) constant time since there are at most 26 lowercase English letters. Building the final string takes O(N).
# Space Complexity: O(N) - We allocate O(N) memory to store the character frequency map and the newly constructed string halves.

from collections import Counter

class Solution:
    def smallestPalindromicRearrangement(self, s: str) -> str:
        # Count the exact frequency of every character
        freq = Counter(s)
        
        left_half = []
        middle = ""
        
        # Process characters in strict alphabetical order ('a' -> 'z')
        for char in sorted(freq.keys()):
            count = freq[char]
            
            # Append exactly half of the occurrences to our left half
            left_half.append(char * (count // 2))
            
            # If the count is odd, this character MUST sit dead center in the palindrome
            if count % 2 == 1:
                middle = char
                
        # Join the left half, add the middle, and mirror the left half for the right
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard odd-length palindrome rearrangement
    print(f"Test 1: {sol.smallestPalindromicRearrangement('cbabc')}") 
    # Expected: "bcacb" 
    # (Counts: a:1, b:2, c:2 -> Left half gets 'b'*1 + 'c'*1 = "bc", middle gets 'a' -> "bc" + "a" + "cb")
    
    # Test 2: Even-length palindrome rearrangement
    print(f"Test 2: {sol.smallestPalindromicRearrangement('bbaabb')}") 
    # Expected: "abbbba" 
    # (Counts: a:2, b:4 -> Left half gets 'a'*1 + 'b'*2 = "abb", middle is "" -> "abb" + "" + "bba")
    
    # Test 3: Already optimal palindrome
    print(f"Test 3: {sol.smallestPalindromicRearrangement('aba')}") 
    # Expected: "aba"