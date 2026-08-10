# Problem: 1510. Stone Game IV
# Difficulty: Hard
# Link: https://leetcode.com/problems/stone-game-iv/description

# Time Complexity: O(N * sqrt(N)) - For each of the N states, we iterate through all valid square numbers up to N, which takes at most sqrt(N) steps.
# Space Complexity: O(N) - We store the boolean win/loss state for every pile size up to N in a 1D DP array.

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] represents whether the current player will WIN starting with i stones
        dp = [False] * (n + 1)
        
        # We build the truth table from 1 stone up to n stones
        for i in range(1, n + 1):
            # Try removing every perfect square <= i
            k = 1
            while k * k <= i:
                # If we can hand the opponent a losing state (False),
                # it means the current state (i) is a winning state
                if not dp[i - k * k]:
                    dp[i] = True
                    break  # Found a winning move, no need to check other squares
                k += 1
                
        # Return the outcome for Alice starting with exactly n stones
        return dp[n]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Alice takes 1 and wins instantly
    print(f"Test 1: {sol.winnerSquareGame(1)}") 
    # Expected: True 
    
    # Test 2: Alice takes 1, Bob takes 1, Alice loses
    print(f"Test 2: {sol.winnerSquareGame(2)}") 
    # Expected: False
    
    # Test 3: Alice takes 4, Bob takes 1, Alice takes 1, Bob takes 1 and wins!
    # Wait, Alice plays optimally! Alice takes 1, leaving 6. Bob takes 4, leaving 2. 
    # Alice takes 1, leaving 1. Bob takes 1. Alice wins!
    print(f"Test 3: {sol.winnerSquareGame(7)}") 
    # Expected: False
    # Actually, 7 evaluates to False. Alice loses with 7!