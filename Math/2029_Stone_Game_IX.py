# Problem: 2029. Stone Game IX
# Difficulty: Medium
# Link: https://leetcode.com/problems/stone-game-ix/description

# Time Complexity: O(N) - We iterate through the array exactly once to count the frequencies modulo 3.
# Space Complexity: O(1) - We only store an array of 3 integers to hold the counts of remainders (0, 1, and 2).

from typing import List

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Step 1: Group all stones by their modulo 3 remainders
        counts = [0, 0, 0]
        for stone in stones:
            counts[stone % 3] += 1
            
        # Step 2: Apply the mathematical Game Theory conditions
        # If the number of 0s (turn-flippers) is Even
        if counts[0] % 2 == 0:
            # Alice wins if she has at least one of both 1s and 2s to start the chain
            return counts[1] > 0 and counts[2] > 0
            
        # If the number of 0s is Odd
        else:
            # Alice needs a severe imbalance to exhaust Bob's supply and force him to lose
            return abs(counts[1] - counts[2]) > 2

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Even 0s, both 1s and 2s present
    print(f"Test 1: {sol.stoneGameIX([2, 1])}") 
    # Expected: True 
    # (Alice picks 1, Bob is forced to pick 2 and makes the sum 3 -> Bob loses)
    
    # Test 2: Only 2s present
    print(f"Test 2: {sol.stoneGameIX([2])}") 
    # Expected: False
    # (Alice picks 2. Bob has no moves left, so Bob wins automatically)
    
    # Test 3: Odd 0s, balanced 1s and 2s
    print(f"Test 3: {sol.stoneGameIX([5, 1, 2, 4, 3])}") 
    # Expected: False