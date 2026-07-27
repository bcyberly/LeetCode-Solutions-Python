# Problem: 1464. Maximum Product of Two Elements in an Array
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description

# Time Complexity: O(N log N) - Sorting the array dominates the execution time.
# Space Complexity: O(1) - Python's in-place sort requires minimal auxiliary memory.

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()

        # Grab the two largest elements from the very end of the array,
        # substract 1 from each, and multiply them together
        return (nums[-1] - 1) * (nums[-2] - 1)
        

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard mix
    print(f"Test 1: {sol.maxProduct([3, 4, 5, 2])}") 
    # Expected: 12 ((5-1) * (4-1) = 4 * 3 = 12)
    
    # Test 2: Identical maximum elements
    print(f"Test 2: {sol.maxProduct([1, 5, 4, 5])}") 
    # Expected: 16 ((5-1) * (5-1) = 4 * 4 = 16)
    
    # Test 3: Minimum array size (two elements)
    print(f"Test 3: {sol.maxProduct([3, 7])}") 
    # Expected: 12 ((7-1) * (3-1) = 6 * 2 = 12)