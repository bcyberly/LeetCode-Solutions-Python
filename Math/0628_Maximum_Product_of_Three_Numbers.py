# Problem: 628. Maximum Product of Three Numbers
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-three-numbers/description

# Time Complexity: O(N log N) - Sorting the array dominates the execution time.
# Space Complexity: O(1) - Python's in-place sort requires minimal auxiliary stack space (or O(N) depending on the underlying Timsort implementation).

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        # Compare the two possible maximum product combinations
        # Option A: The three largest numbers at the very end of the array
        prod3_largest = nums[-1] * nums[-2] * nums[-3]
        
        # Option B: The two smallest (most negative) numbers at the front, multiplied by the largest number
        prod2_smallest_1_largest = nums[0] * nums[1] * nums[-1]
        
        return max(prod3_largest, prod2_smallest_1_largest)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: All positive integers
    print(f"Test 1: {sol.maximumProduct([1, 2, 3, 4])}") 
    # Expected: 24 (2 * 3 * 4 = 24)
    
    # Test 2: Large negative numbers trap
    print(f"Test 2: {sol.maximumProduct([-10, -10, 1, 2, 3])}") 
    # Expected: 300 (-10 * -10 * 3 = 300)
    
    # Test 3: Mixed zeros and negatives
    print(f"Test 3: {sol.maximumProduct([-1, -2, -3])}") 
    # Expected: -6 (-1 * -2 * -3 = -6)