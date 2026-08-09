# Problem: 1140. Stone Game II
# Difficulty: Medium
# Link: https://leetcode.com/problems/stone-game-ii/description

# Time Complexity: O(N³) - There are N possible indices and N possible values for M, meaning O(N²) states. In each state, we run a loop of up to 2M (which is bounded by N), leading to O(N³) total time.
# Space Complexity: O(N²) - The memoization cache stores up to N * N unique state evaluations, and the recursion stack reaches a maximum depth of N.

from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precompute suffix sums so we can find out how many stones 
        # remain from pile[i] to the end in strict O(1) time.
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            # Base Case: If we can reach the end of the array, we take all remaining stones!
            if i + 2 * m >= n:
                return suffix_sum[i]
            
            best_score = 0
            
            # Try every valid move: taking X piles where 1 <= X <= 2M
            for x in range(1, 2 * m + 1):
                # The opponent will play optimally from index i + X with new multiplier max(m, X)
                opponent_score = dp(i + x, max(m, x))
                
                # Our score is ALL the remaining stones on the table, minus what the opponent takes
                our_score = suffix_sum[i] - opponent_score
                
                if our_score > best_score:
                    best_score = our_score
                    
            return best_score
            
        return dp(0, 1)

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard game progression
    print(f"Test 1: {sol.stoneGameII([2, 7, 9, 4, 4])}") 
    # Expected: 10 
    # (Alice takes 2. Bob takes 7, 9. Alice takes 4, 4.)
    
    # Test 2: Alice dominates by manipulating M
    print(f"Test 2: {sol.stoneGameII([1, 2, 3, 4, 5, 100])}") 
    # Expected: 104