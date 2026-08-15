# Problem: 3702. Longest Subsequence With Non-Zero Bitwise XOR
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-subsequence-with-non-zero-bitwise-xor/description

# Time Complexity: O(N) - We perform a single linear sweep over the array to compute the global XOR sum and check for non-zero elements.
# Space Complexity: O(1) - We only track a couple of integer/boolean variables regardless of the input size.

from typing import List

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_nonzero = False
        
        # O(N) Single Pass: Calculate total XOR and look for any non-zero element
        for num in nums:
            total_xor ^= num
            if num != 0:
                has_nonzero = True
                
        # Case 1: The array is entirely made of zeroes. No non-zero XOR is possible
        if not has_nonzero:
            return 0
            
        # Case 2: The entire array already yields a non-zero XOR
        if total_xor != 0:
            return len(nums)
            
        # Case 3: The total XOR is 0, but non-zero elements exist
        # Removing exactly ONE non-zero element will instantly unbalance the XOR to a non-zero state
        return len(nums) - 1

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Total XOR is 0, but non-zero elements exist
    print(f"Test 1: {sol.longestSubsequence([1, 2, 3])}") 
    # Expected: 2 
    # (1^2^3 = 0. Remove any one element, e.g., [1, 2] -> 1^2 = 3 != 0)
    
    # Test 2: Entire array works
    print(f"Test 2: {sol.longestSubsequence([3, 4, 5])}") 
    # Expected: 3
    # (3^4^5 = 2 != 0)
    
    # Test 3: Array of zeroes
    print(f"Test 3: {sol.longestSubsequence([0, 0, 0])}") 
    # Expected: 0