# Problem: 2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description

# Time Complexity: O(N) - We iterate through the array once to find the prefix sum, and building the Hash Set takes O(N). The while loop runs at most N times, keeping everything strictly linear.
# Space Complexity: O(N) - We store the unique elements of the array in a Hash Set for O(1) constant-time lookups.

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Calculate the longest sequential prefix sum starting from index 0
        prefix_sum = nums[0]
        
        for i in range(1, len(nums)):
            # If the sequence breaks, we stop immediately!
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
                
        # Step 2: Convert to a Hash Set for instant O(1) lookups
        num_set = set(nums)
        
        # Step 3: Increment the sum until we find a number NOT in the array
        x = prefix_sum
        while x in num_set:
            x += 1
            
        return x

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Sequence breaks early
    print(f"Test 1: {sol.missingInteger([1, 2, 3, 2, 5])}") 
    # Expected: 6 
    # (Prefix is [1, 2, 3] -> Sum = 6. 6 is not in the array!)
    
    # Test 2: Sum exists in the array, requires incrementing
    print(f"Test 2: {sol.missingInteger([3, 4, 5, 1, 12, 14, 13])}") 
    # Expected: 15
    # (Prefix is [3, 4, 5] -> Sum = 12. 12, 13, 14 are in the array, so we increment to 15!)