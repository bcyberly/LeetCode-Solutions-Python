# Problem: 3518. Smallest Palindromic Rearrangement II
# Difficulty: Hard
# Link: https://leetcode.com/problems/smallest-palindromic-rearrangement-ii/description

# Time Complexity: O(N) - Calculating initial factorials takes O(N). Building the string takes O(N * 26), which collapses to O(N) time.
# Space Complexity: O(N) - We allocate O(N) memory to store the character frequency map and the newly constructed string halves.

from collections import Counter
import math

class Solution:
    def kThSmallestPalindromicPermutation(self, s: str, k: int) -> str:
        # Count exact frequencies to separate the left half and the middle
        freq = Counter(s)
        
        left_counts = {}
        middle = ""
        
        for char in sorted(freq.keys()):
            count = freq[char]
            if count % 2 == 1:
                middle = char
            left_counts[char] = count // 2
            
        N = sum(left_counts.values())
        
        # Calculate the total initial permutations for the left half: P = N! / (c1! * c2! ...)
        P = math.factorial(N)
        for count in left_counts.values():
            P //= math.factorial(count)
            
        # If they ask for a permutation that doesn't exist, return empty string
        if k > P:
            return ""
            
        left_half = []
        
        # Build the k-th permutation dynamically position by position
        for _ in range(N):
            for char in left_counts.keys():
                if left_counts[char] > 0:
                    # Calculate how many permutations exist if we place 'char' in this exact slot
                    # The math beautifully simplifies to just: old_perms * (char_count / remaining_length)
                    sub_perms = P * left_counts[char] // N
                    
                    if k <= sub_perms:
                        # The k-th permutation resides inside this character's block! Lock it in.
                        left_half.append(char)
                        P = sub_perms
                        left_counts[char] -= 1
                        N -= 1
                        break
                    else:
                        # The k-th permutation is further down the alphabetical list
                        # Skip this entire block of combinations instantly
                        k -= sub_perms
                        
        # Join the left half, add the middle, and mirror the left half for the right
        left_str = "".join(left_half)
        return left_str + middle + left_str[::-1]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: First permutation (matches Part I)
    print(f"Test 1: {sol.kThSmallestPalindromicPermutation('bbaabb', 1)}") 
    # Expected: "abbbba" (Left half: abb)
    
    # Test 2: Second permutation
    print(f"Test 2: {sol.kThSmallestPalindromicPermutation('bbaabb', 2)}") 
    # Expected: "babbab" (Left half: bab)
    
    # Test 3: k exceeds total permutations
    print(f"Test 3: {sol.kThSmallestPalindromicPermutation('aba', 2)}") 
    # Expected: "" (Only 1 valid palindrome exists: 'aba')