# Problem: 1927. Sum Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-game/description

# Time Complexity: O(N) - We perform a single linear sweep across the string to tally the sums and question mark counts for both halves.
# Space Complexity: O(1) - We only store four integer variables (sum1, sum2, q1, q2) regardless of the string's length.

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        sum1 = sum2 = 0
        q1 = q2 = 0
        
        # Parse the first half of the string
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                sum1 += int(num[i])
                
        # Parse the second half of the string
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                sum2 += int(num[i])
                
        # Game Theory Evaluation
        # If the total number of '?' is odd, Alice gets the last move.
        # She can always choose a digit that prevents the sums from being equal.
        if (q1 + q2) % 2 != 0:
            return True
            
        # If the total is even, Bob gets the last move.
        # Bob pairs up the '?'s. Every extra pair on one side can be forced to sum to exactly 9.
        # We check if Bob's forced additions perfectly neutralize the initial sum difference.
        if (sum1 - sum2) + (q1 - q2) // 2 * 9 == 0:
            return False  # Bob successfully balances the scale
            
        return True       # Alice wins because Bob mathematically cannot balance it

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Total '?' is odd -> Alice automatically wins
    print(f"Test 1: {sol.sumGame('5023')}") 
    # Expected: False 
    # Wait, '5023' has 0 '?' which is even!
    # sum1 = 5, sum2 = 5. diff = 0. q1 = 0, q2 = 0. 0 + 0 = 0 -> Bob wins! 
    # Output: False
    
    # Test 2: Odd '?'
    print(f"Test 2: {sol.sumGame('25??')}") 
    # Expected: True
    # (2 '?' total. sum1 = 7, sum2 = 0. q1 = 0, q2 = 2. 7 + (-2 // 2)*9 = 7 - 9 = -2 != 0 -> Alice wins)
    
    # Test 3: Bob can perfectly balance the board
    print(f"Test 3: {sol.sumGame('?3295???')}") 
    # Expected: False