# Problem: 3731. Find Missing Elements
# Difficulty: Easy
# Link: https://leetcode.com/problems/find-missing-elements/description

# Time Complexity: O(N + R) - Where N is the number of elements and R is the range from min to max. Finding min/max and building the set takes O(N). Sweeping the range takes O(R).
# Space Complexity: O(N) - We store the given array in a Hash Set for O(1) constant-time lookups.

from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        # Find our boundaries
        min_val = min(nums)
        max_val = max(nums)

        # Convert the list to a Hash Set for instant O(1) lookups
        num_set = set(nums)
        missing = []

        # Sweep through the exact original range
        for i in range(min_val, max_val + 1):
            if i not in num_set:
                missing.append(i)

        # Because our ranfe goes from smallest to largest, the output is naturally sorted
        return missing

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard missing elements
    print(f"Test 1: {sol.findMissingElements([4, 1, 6, 2])}") 
    # Expected: [3, 5] (Original range: 1 to 6)
    
    # Test 2: No missing elements
    print(f"Test 2: {sol.findMissingElements([1, 2, 3, 4])}") 
    # Expected: []
    
    # Test 3: Large gap
    print(f"Test 3: {sol.findMissingElements([10, 15])}") 
    # Expected: [11, 12, 13, 14]