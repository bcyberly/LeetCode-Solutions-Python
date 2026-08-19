# Problem: 1386. Cinema Seat Allocation
# Difficulty: Medium
# Link: https://leetcode.com/problems/cinema-seat-allocation/description

# Time Complexity: O(M) - Where M is the length of reservedSeats. We process each reservation exactly once, and the bitwise evaluations take strict O(1) time.
# Space Complexity: O(M) - We store at most M unique rows in our Hash Map. We bypass O(N) memory allocation entirely.

from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map reservations into bitmasks by row
        reserved = defaultdict(int)
        for r, c in reservedSeats:
            # We flip the c-th bit to 1 to mark the seat as reserved
            reserved[r] |= (1 << c)
            
        # Assume the cinema is completely empty
        # An empty row perfectly fits 2 families
        max_groups = 2 * n
        
        # Define our block bitmasks
        left_mask = (1 << 2) | (1 << 3) | (1 << 4) | (1 << 5)
        right_mask = (1 << 6) | (1 << 7) | (1 << 8) | (1 << 9)
        middle_mask = (1 << 4) | (1 << 5) | (1 << 6) | (1 << 7)
        
        # Only evaluate rows that actually have reservations
        for row_mask in reserved.values():
            # Remove the 2 families we preemptively assumed could sit here
            max_groups -= 2
            
            # Check availability using Bitwise AND
            # If the result is 0, it means NO reserved seats overlap with our block
            if (row_mask & left_mask) == 0 and (row_mask & right_mask) == 0:
                max_groups += 2
            elif (row_mask & left_mask) == 0 or (row_mask & right_mask) == 0 or (row_mask & middle_mask) == 0:
                max_groups += 1
                
        return max_groups

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard cinema allocations
    print(f"Test 1: {sol.maxNumberOfFamilies(3, [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]])}") 
    # Expected: 4 
    # (Row 1 fits 1 Middle. Row 2 fits 1 Left. Row 3 fits 2 (Seats 1 and 10 are irrelevant!))
    
    # Test 2: Row entirely blocked
    print(f"Test 2: {sol.maxNumberOfFamilies(2, [[2,1],[1,8],[2,6]])}") 
    # Expected: 2
    
    # Test 3: Only the middle block is available
    print(f"Test 3: {sol.maxNumberOfFamilies(4, [[4,3],[1,4],[4,6],[1,7]])}") 
    # Expected: 4