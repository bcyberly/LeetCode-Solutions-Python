# Problem: 486. Predict the Winner
# Difficulty: Medium
# Link: https://leetcode.com/problems/predict-the-winner/description

# Time Complexity: O(N^2) - We evaluate every possible contiguous subarray exactly once using memoization.
# Space Complexity: O(N^2) - The recursion stack and memoization cache scale with the number of possible subarrays.

from typing import List
from functools import cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # If the array has an even number of elements, Player 1 can always force a win
        # by choosing to strictly collect either all even-indexed or all odd-indexed elements
        if len(nums) % 2 == 0:
            return True
            
        # dp(left, right) returns the maximum score difference the CURRENT player 
        # can achieve against their opponent from the subarray nums[left...right]
        @cache
        def dp(left: int, right: int) -> int:
            # Base case: Only one number left, the current player takes it
            if left == right:
                return nums[left]
                
            # Take the left element
            # We subtract dp(left + 1, right) because the next turn belongs to the opponent
            pick_left = nums[left] - dp(left + 1, right)
            
            # Take the right element
            pick_right = nums[right] - dp(left, right - 1)
            
            # The current player plays optimally, so they maximize their net difference
            return max(pick_left, pick_right)
            
        # Player 1 wins if they can achieve a net difference >= 0 from the entire array
        return dp(0, len(nums) - 1) >= 0

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Player 1 cannot win against optimal play
    print(f"Test 1: {sol.predictTheWinner([1, 5, 2])}") 
    # Expected: False 
    # (P1 picks 1 or 2. P2 immediately picks the massive 5 and wins.)
    
    # Test 2: Player 1 wins via optimal early sacrifice
    print(f"Test 2: {sol.predictTheWinner([1, 5, 233, 7])}") 
    # Expected: True 
    # (Even length! P1 picks 1, P2 picks 5, P1 picks 233 and dominates.)