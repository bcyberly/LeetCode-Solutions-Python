# Problem: 3310. Remove Methods From Project
# Difficulty: Medium
# Link: https://leetcode.com/problems/remove-methods-from-project/description

# Time Complexity: O(V + E) - Where V is the number of methods (n) and E is the number of invocations. Building the graph, running BFS, and the final edge scan each take linear time.
# Space Complexity: O(V + E) - We store the graph as an adjacency list and keep a Set/Queue for the suspicious methods.

from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build the directed graph using an adjacency list
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)
            
        # The Infection Phase (Find all suspicious methods)
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        # The Isolation Check
        # We cannot remove the suspicious group if a healthy method depends on a suspicious one
        can_remove = True
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                can_remove = False
                break
                
        # Return the appropriate remaining methods
        if can_remove:
            # Return all methods that are NOT suspicious
            return [i for i in range(n) if i not in suspicious]
        else:
            # If we can't remove them, return all methods intact
            return list(range(n))

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Valid removal
    print(f"Test 1: {sol.remainingMethods(4, 1, [[1, 2], [0, 1], [3, 2]])}") 
    # Expected: [0, 1, 2, 3] 
    # (Wait! Method 0 (healthy) calls Method 1 (suspicious), so we CANNOT remove them!)
    
    # Test 2: Successful isolation
    print(f"Test 2: {sol.remainingMethods(5, 0, [[1, 2], [0, 2], [0, 1], [3, 4]])}") 
    # Expected: [3, 4] 
    # (Bug is at 0. It calls 1 and 2. Nobody else calls 0, 1, or 2. We remove 0, 1, 2!)
    
    # Test 3: No invocations
    print(f"Test 3: {sol.remainingMethods(3, 2, [])}") 
    # Expected: [0, 1] 
    # (Bug at 2. It calls nothing. Nobody calls it. We just remove 2.)