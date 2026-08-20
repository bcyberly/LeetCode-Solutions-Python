# Problem: 3069. Distribute Elements Into Two Arrays I
# Difficulty: Easy
# Link: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/description

# Time Complexity: O(N) - We iterate through the elements of the array exactly once. The list append operations and the tail lookups arr[-1] take O(1) time.
# Space Complexity: O(N) - We allocate memory for arr1 and arr2, which together will store exactly N elements.

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # Initialize the arrays with the first two elements
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        
        # Iterate through the remaining elements
        for i in range(2, len(nums)):
            # Compare the LAST elements of both arrays
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
                
        # Concatenate and return the result
        return arr1 + arr2

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard alternation
    print(f"Test 1: {sol.resultArray([2, 1, 3])}") 
    # Expected: [2, 3, 1] 
    # (arr1 gets 2, arr2 gets 1. 3 goes to arr1 because 2 > 1. Result: [2, 3] + [1])
    
    # Test 2: One array dominates
    print(f"Test 2: {sol.resultArray([5, 4, 3, 8])}") 
    # Expected: [5, 3, 4, 8]
    # (arr1 gets 5, arr2 gets 4. 3 goes to arr1 (5 > 4). 8 goes to arr2 (3 < 4). Result: [5, 3] + [4, 8])