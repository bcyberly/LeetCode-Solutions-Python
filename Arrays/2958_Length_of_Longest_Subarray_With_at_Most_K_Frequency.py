# Problem: 2958. Length of Longest Subarray With at Most K Frequency
# Difficulty: Medium
# Link: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description

# Time Complexity: O(N) - Both the left and right pointers only move forward, visiting each element at most twice.
# Space Complexity: O(N) - In the worst case (where all elements are unique), the Hash Map stores N distinct key-value pairs.

from typing import List
from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_len = 0
        
        # The right pointer expands the window
        for right in range(len(nums)):
            freq[nums[right]] += 1
            
            # If the current element exceeds the allowed frequency 'k', 
            # we must shrink the window from the left until it is valid again
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            # Calculate the maximum valid window size seen so far
            max_len = max(max_len, right - left + 1)
            
        return max_len

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard Sliding Window
    print(f"Test 1: {sol.maxSubarrayLength([1, 2, 3, 1, 2, 3, 1, 2], 2)}") 
    # Expected: 6 
    # (Longest valid subarray is [1, 2, 3, 1, 2, 3] or [2, 3, 1, 2, 3, 1])
    
    # Test 2: Early Break
    print(f"Test 2: {sol.maxSubarrayLength([1, 2, 1, 2, 1, 2, 1, 2], 1)}") 
    # Expected: 2
    
    # Test 3: K is large enough for the whole array
    print(f"Test 3: {sol.maxSubarrayLength([5, 5, 5, 5, 5, 5, 5], 4)}") 
    # Expected: 4