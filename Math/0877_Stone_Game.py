# Problem: 877. Stone Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/stone-game/description

# Time Complexity: O(1) - The game is mathematically rigged. We don't even need to look at the array.
# Space Complexity: O(1) - No memory is used.

from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Since the number of piles is strictly even, Alice can strategically 
        # choose to take ONLY the even-indexed piles or ONLY the odd-indexed piles.
        # She just calculates which sum is larger beforehand, and perfectly mirrors 
        # Bob's moves to guarantee she gets the larger half. 
        # Therefore, Alice ALWAYS wins.
        return True

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard game
    print(f"Test 1: {sol.stoneGame([5, 3, 4, 5])}") 
    # Expected: True 
    
    # Test 2: Massive array
    print(f"Test 2: {sol.stoneGame([3, 7, 2, 3])}") 
    # Expected: True