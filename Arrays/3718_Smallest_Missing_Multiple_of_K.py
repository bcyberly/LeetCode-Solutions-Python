# Problem: 3718. Smallest Missing Multiple of K
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-missing-multiple-of-k/description

# Time Complexity: O(N) - We iterate through the array once to build the Hash Set. The while loop runs at most (N + 1) times, keeping execution strictly linear.
# Space Complexity: O(N) - We store the unique elements of the array in a Hash Set to guarantee O(1) constant-time lookups.

from typing import List

class Solution:
    def smallestMissingMultiple(self, nums: List[int], k: int) -> int:
        # Convert the array to a Hash Set for instant O(1) lookups
        num_set = set(nums)

        # Start with the first positive multiple of k
        multiple = k

        # Keep incrementing by k until we find a missing number
        while multiple in num_set:
            multiple += k

        return multiple

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Missing early multiple
    print(f"Test 1: {sol.smallestMissingMultiple([1, 2, 3], 2)}") 
    # Expected: 4 
    # (Multiples of 2 are: 2, 4, 6. The array has 2. It is missing 4!)
    
    # Test 2: Standard progression
    print(f"Test 2: {sol.smallestMissingMultiple([3, 6, 9], 3)}") 
    # Expected: 12
    # (Array has 3, 6, 9. The next multiple is 12.)
    
    # Test 3: First multiple is already missing
    print(f"Test 3: {sol.smallestMissingMultiple([1, 2, 4], 5)}") 
    # Expected: 5
    # (The array doesn't even have 5, so we return it instantly!)