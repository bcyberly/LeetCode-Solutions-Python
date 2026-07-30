# Problem: 3014. Minimum Number of Pushes to Type Word I
# Difficulty: Easy
# Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-i/description

# Time Complexity: O(1) - The loop runs a maximum of 4 times regardless of input, since the alphabet only has 26 distinct letters.
# Space Complexity: O(1) - No auxiliary data structures are used.

class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        total_pushes = 0
        multiplier = 1
        
        # We fill our 8 telephone keys tier by tier
        while n > 0:
            # We can place up to 8 letters at the current push depth
            current_batch = min(8, n)
            
            # Add the cost of this tier to our total
            total_pushes += current_batch * multiplier
            
            # Deduct the placed letters and move to the next push depth
            n -= current_batch
            multiplier += 1
            
        return total_pushes

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Length <= 8 (All letters cost 1 push)
    print(f"Test 1: {sol.minimumPushes('abcde')}") 
    # Expected: 5 (5 letters * 1 push each = 5)
    
    # Test 2: Spills into Tier 2
    print(f"Test 2: {sol.minimumPushes('xycdefghij')}") 
    # Expected: 12 (8 letters * 1 push + 2 letters * 2 pushes = 12)
    
    # Test 3: The maximum possible distinct string (26 letters)
    print(f"Test 3: {sol.minimumPushes('abcdefghijklmnopqrstuvwxyz')}") 
    # Expected: 56 (8*1 + 8*2 + 8*3 + 2*4 = 8 + 16 + 24 + 8 = 56)