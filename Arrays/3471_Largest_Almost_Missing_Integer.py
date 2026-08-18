# Problem: 3471. Find the Largest Almost Missing Integer
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-the-largest-almost-missing-integer/description

# Time Complexity: O(N * K) - We iterate through (N - K + 1) subarrays, and for each, we create a set of size K. 
# Space Complexity: O(N) - We store the frequency of unique elements in a Hash Map, which scales with the number of unique elements in the array.

from typing import List
from collections import defaultdict

class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # Dictionary to count in how many DISTINCT subarrays of size k an element appears
        subarray_counts = defaultdict(int)
        
        # Step 1: Slide a window of size k across the array
        for i in range(n - k + 1):
            # Extract the subarray and find its unique elements
            window = nums[i:i + k]
            unique_in_window = set(window)
            
            # Step 2: Tally a vote for each unique element present in this specific window
            for num in unique_in_window:
                subarray_counts[num] += 1
                
        # Step 3: Find the largest integer that received exactly 1 vote
        largest_almost_missing = -1
        
        for num, count in subarray_counts.items():
            if count == 1:
                largest_almost_missing = max(largest_almost_missing, num)
                
        return largest_almost_missing

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Element appears in exactly one subarray
    print(f"Test 1: {sol.largestInteger([3, 9, 2, 1, 7], 3)}") 
    # Expected: 7 
    # (Subarrays: [3,9,2], [9,2,1], [2,1,7]. 7 only appears in the last one!)
    
    # Test 2: Same K as array length
    print(f"Test 2: {sol.largestInteger([3, 9, 2, 1, 7], 5)}") 
    # Expected: 9
    # (Only 1 subarray exists. ALL elements appear exactly once. 9 is the max.)
    
    # Test 3: No valid integer
    print(f"Test 3: {sol.largestInteger([0, 0], 1)}") 
    # Expected: -1
    # (Subarrays of size 1: [0], [0]. 0 appears in TWO subarrays, so none have count 1.)