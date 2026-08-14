# Problem: 3090. Maximum Length Substring With Two Occurrences
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description

# Time Complexity: O(N) - Both the left and right pointers only move forward, scanning in linear time.
# Space Complexity: O(1) - The frequency map stores at most 26 lowercase English letters, keeping auxiliary space strictly constant.
from collections import defaultdict

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0

        # The right pointer expands our string window
        for right in range(len(s)):
            freq[s[right]] += 1

            # If the current character appears more than 2 times, the window is invalid
            # Shrink from the left until the offending character's count is <= 2
            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1

            # Record the maximum valid window size seen so far
            max_len = max(max_len, right - left + 1)


        return max_len

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Sliding Window
    print(f"Test 1: {sol.maximumLengthSubstring('bcbbbcba')}") 
    # Expected: 4 
    # (Longest valid substring is "bcba")
    
    # Test 2: Valid entire string
    print(f"Test 2: {sol.maximumLengthSubstring('aaaa')}") 
    # Expected: 2
    # (Longest valid is "aa")
    
    # Test 3: No shrinking required
    print(f"Test 3: {sol.maximumLengthSubstring('abcdef')}") 
    # Expected: 6