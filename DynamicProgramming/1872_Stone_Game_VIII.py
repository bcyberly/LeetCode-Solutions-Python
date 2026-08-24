# Problem: 1872. Stone Game VIII
# Difficulty: Hard
# Link: https://leetcode.com/problems/stone-game-viii/description

# Time Complexity: O(N) - We perform one linear pass to calculate prefix sums, and one reverse linear pass to compute the DP state.
# Space Complexity: O(1) - We mutate the input array in-place to store the prefix sums and track the DP state using a single integer variable.

from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Calculate the prefix sums in-place
        for i in range(1, n):
            stones[i] += stones[i - 1]
            
        # Bottom-Up DP
        # Base Case: If we are forced to the very last index, we MUST take all remaining stones
        # The score difference is simply the total sum, and the opponent gets 0
        dp = stones[-1]
        
        # Iterate backwards from the second-to-last choice down to index 1
        # We stop at 1 because the rules state we must choose x > 1 (0-indexed minimum is 1)
        for i in range(n - 2, 0, -1):
            # We either SKIP this prefix (keeping our best future dp), 
            # or we TAKE this prefix (getting stones[i] and subtracting the opponent's best future dp)
            dp = max(dp, stones[i] - dp)
            
        return dp

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard game
    print(f"Test 1: {sol.stoneGameVIII([-1, 2, -3, 4, -5])}") 
    # Expected: 5 
    
    # Test 2: All positive numbers
    print(f"Test 2: {sol.stoneGameVIII([7, -6, 5, 10, 5, -2, -6])}") 
    # Expected: 13
    
    # Test 3: Only two stones
    print(f"Test 3: {sol.stoneGameVIII([1, 2])}") 
    # Expected: 3
    # (Alice must take x > 1, so she takes both. Sum = 3. Bob gets 0.)