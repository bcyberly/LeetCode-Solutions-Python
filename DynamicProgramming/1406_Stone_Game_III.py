# Problem: 1406. Stone Game III
# Difficulty: Hard
# Link: https://leetcode.com/problems/stone-game-iii/description

# Time Complexity: O(N) - We iterate through the array backwards exactly once, checking at most 3 options per element.
# Space Complexity: O(N) - We allocate a 1D DP array of size N + 1.

from typing import List
import math

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i] represents the max net score difference the current player 
        # can achieve starting from index i.
        # We need an array of size n + 1 to handle the base case where no stones remain
        dp = [0] * (n + 1)
        
        # We build the answer from the back of the line to the front
        for i in range(n - 1, -1, -1):
            best_net_score = -math.inf
            stones_taken = 0
            
            # The player can take 1, 2, or 3 stones (as long as they exist)
            for k in range(3):
                if i + k < n:
                    stones_taken += stoneValue[i + k]
                    
                    # The current player's net score is what they just took, 
                    # MINUS what the opponent will achieve optimally from the remaining stones
                    best_net_score = max(best_net_score, stones_taken - dp[i + k + 1])
                    
            dp[i] = best_net_score
            
        # If the net difference from the starting line is > 0, Alice wins
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Tie game
    print(f"Test 1: {sol.stoneGameIII([1, 2, 3, 7])}") 
    # Expected: "Bob" 
    # (Alice takes 1, 2, and 3. Bob takes 7 and wins. If Alice takes 1, Bob takes 2, 3, 7!)
    
    # Test 2: Alice dominates
    print(f"Test 2: {sol.stoneGameIII([1, 2, 3, -9])}") 
    # Expected: "Alice"
    
    # Test 3: Strategic tie
    print(f"Test 3: {sol.stoneGameIII([1, 2, 3, 6])}") 
    # Expected: "Tie"