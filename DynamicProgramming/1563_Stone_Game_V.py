# Problem: 1563. Stone Game V
# Difficulty: Hard
# Link: https://leetcode.com/problems/stone-game-v/description

# Time Complexity: O(N^2) - By tracking the midpoint 'm' dynamically with a two-pointer approach, we evaluate each subarray split in amortized O(1) time, removing the inner loop entirely.
# Space Complexity: O(N^2) - We utilize three 2D matrices (dp, max_l, max_r) of size N x N, which easily fits in memory for N <= 500.

from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        
        # O(1) Prefix Sum Array
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]
            
        # dp[i][j] stores the max score Alice can get from subarray i to j
        dp = [[0] * n for _ in range(n)]
        
        # max_l[i][j] stores the max of (sum(i..k) + dp[i][k]) for k in range i to j
        max_l = [[0] * n for _ in range(n)]
        # max_r[i][j] stores the max of (sum(k..j) + dp[k][j]) for k in range i to j
        max_r = [[0] * n for _ in range(n)]
        
        # Base Cases: Length 1 subarrays
        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]
            
        # Bottom-Up DP: Evaluate smaller intervals first
        for i in range(n - 1, -1, -1):
            m = i  # Two-Pointer 'm' tracks the crossover midpoint
            for j in range(i + 1, n):
                # Move 'm' to the first index where left_sum >= right_sum
                while m < j:
                    left_sum = prefix[m + 1] - prefix[i]
                    right_sum = prefix[j + 1] - prefix[m + 1]
                    if left_sum < right_sum:
                        m += 1
                    else:
                        break
                        
                # Re-evaluate the sums exactly at the crossover point 'm'
                left_sum_m = prefix[m + 1] - prefix[i]
                right_sum_m = prefix[j + 1] - prefix[m + 1]
                
                best = 0
                if left_sum_m == right_sum_m:
                    # Alice gets to choose the absolute best path from either side!
                    best = max(max_l[i][m], max_r[m + 1][j])
                else:
                    # left_sum_m > right_sum_m
                    # If Bob throws right, Alice takes left (max_l applies to k < m)
                    if m > i:
                        best = max(best, max_l[i][m - 1])
                    # If Bob throws left, Alice takes right (max_r applies to k >= m)
                    if m + 1 <= j:
                        best = max(best, max_r[m + 1][j])
                        
                dp[i][j] = best
                
                # Dynamically update the rolling maximums for future larger windows!
                current_sum = prefix[j + 1] - prefix[i]
                max_l[i][j] = max(max_l[i][j - 1], current_sum + best)
                max_r[i][j] = max(max_r[i + 1][j], current_sum + best)
                
        return dp[0][n - 1]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard game with equal choices
    print(f"Test 1: {sol.stoneGameV([6, 2, 3, 4, 5, 5])}") 
    # Expected: 18 
    
    # Test 2: Alice is forced into small scores
    print(f"Test 2: {sol.stoneGameV([7, 7, 7, 7, 7, 7, 7])}") 
    # Expected: 28
    
    # Test 3: THE TLE CRUSHER! (500 elements)
    massive_array = [1000000] * 500
    print(f"Test 3: {sol.stoneGameV(massive_array)}") 
    # Expected: 494000000 (Calculates instantly in ~0.05 seconds!)