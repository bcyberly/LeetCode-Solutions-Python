# Problem: 3116. Kth Smallest Amount With Single Denomination Combination
# Difficulty: Hard
# Link: https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description

# Time Complexity: O(2^N * log(min(coins) * k)) - Precomputing the 2^N LCMs takes O(N * 2^N). The binary search takes logarithmic time relative to the search space, evaluating the 2^N precomputed combinations at each step.
# Space Complexity: O(2^N) - We store the LCM and inclusion/exclusion sign for all possible non-empty subsets of the coins.

import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        subsets = []
        
        # Precompute the LCM and the Inclusion-Exclusion sign for all subsets
        # We iterate from 1 to (2^N - 1) to generate all non-empty subsets using bitmasking
        for i in range(1, 1 << n):
            current_lcm = 1
            set_bits = 0
            
            for j in range(n):
                if i & (1 << j):
                    set_bits += 1
                    # Python 3.9+ supports math.lcm
                    current_lcm = math.lcm(current_lcm, coins[j])
                    
            # If the subset has an odd number of elements, we ADD it (+1)
            # If it has an even number of elements, we SUBTRACT it (-1)
            sign = 1 if set_bits % 2 == 1 else -1
            subsets.append((current_lcm, sign))
            
        # Helper function to count valid amounts <= x using PIE
        def count_valid_amounts(x: int) -> int:
            total_count = 0
            for lcm_val, sign in subsets:
                total_count += sign * (x // lcm_val)
            return total_count

        # Binary Search on the Answer
        left = 1
        # The absolute maximum possible value occurs if we only use the smallest coin
        right = min(coins) * k
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            if count_valid_amounts(mid) >= k:
                ans = mid
                right = mid - 1  # Try to find a smaller valid amount
            else:
                left = mid + 1   # We haven't reached the k-th amount yet
                
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Simple progression
    print(f"Test 1: {sol.findKthSmallest([3, 6, 9], 3)}") 
    # Expected: 9 
    # (Valid amounts: 3, 6, 9, 12, 15... The 3rd smallest is 9)
    
    # Test 2: Overlapping multiples requiring Inclusion-Exclusion
    print(f"Test 2: {sol.findKthSmallest([5, 2], 7)}") 
    # Expected: 12
    # (Valid amounts: 2, 4, 5, 6, 8, 10, 12... The 7th smallest is 12)