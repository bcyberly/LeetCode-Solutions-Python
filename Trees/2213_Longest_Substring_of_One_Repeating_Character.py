# Problem: 2213. Longest Substring of One Repeating Character
# Difficulty: Hard
# Link: https://leetcode.com/problems/longest-substring-of-one-repeating-character/description

# Time Complexity: O(N + K log N) - Building the segment tree takes O(N) time. Processing each of the K queries requires traversing down and back up the tree height, taking O(log N) time per query.
# Space Complexity: O(N) - We allocate multiple parallel arrays of size 4*N to represent the Segment Tree state nodes, keeping auxiliary space strictly linear.

from typing import List

class SegmentTree:
    def __init__(self, s: str):
        self.n = len(s)
        size = 4 * self.n + 1
        
        # Parallel arrays to avoid Python object overhead (bypasses TLE)
        self.max_len = [0] * size
        self.pref_len = [0] * size
        self.suff_len = [0] * size
        self.pref_char = [''] * size
        self.suff_char = [''] * size
        
        self.s = s
        self.build(1, 0, self.n - 1)
        
    def merge(self, node: int, L: int, mid: int, R: int):
        left_child = 2 * node
        right_child = 2 * node + 1
        
        # Edge Characters pass upwards directly from the extreme ends
        self.pref_char[node] = self.pref_char[left_child]
        self.suff_char[node] = self.suff_char[right_child]
        
        len_left = mid - L + 1
        len_right = R - mid
        
        # Update Prefix Length
        # If the entire left child is one solid block AND it matches the right child's start
        if self.pref_len[left_child] == len_left and self.suff_char[left_child] == self.pref_char[right_child]:
            self.pref_len[node] = len_left + self.pref_len[right_child]
        else:
            self.pref_len[node] = self.pref_len[left_child]
            
        # Update Suffix Length
        # If the entire right child is one solid block AND it matches the left child's end
        if self.suff_len[right_child] == len_right and self.suff_char[left_child] == self.pref_char[right_child]:
            self.suff_len[node] = len_right + self.suff_len[left_child]
        else:
            self.suff_len[node] = self.suff_len[right_child]
            
        # Update the Global Maximum Length for this node
        self.max_len[node] = max(self.max_len[left_child], self.max_len[right_child])
        
        # The ultimate bridge check: Do the two chunks connect seamlessly in the middle?
        if self.suff_char[left_child] == self.pref_char[right_child]:
            bridged_len = self.suff_len[left_child] + self.pref_len[right_child]
            if bridged_len > self.max_len[node]:
                self.max_len[node] = bridged_len

    def build(self, node: int, L: int, R: int):
        # Base Case: Single Character Leaf Node
        if L == R:
            char = self.s[L]
            self.max_len[node] = 1
            self.pref_len[node] = 1
            self.suff_len[node] = 1
            self.pref_char[node] = char
            self.suff_char[node] = char
            return
            
        mid = (L + R) // 2
        self.build(2 * node, L, mid)
        self.build(2 * node + 1, mid + 1, R)
        self.merge(node, L, mid, R)
        
    def update(self, node: int, L: int, R: int, idx: int, char: str):
        # Base Case: We found the exact character to mutate
        if L == R:
            self.pref_char[node] = char
            self.suff_char[node] = char
            return
            
        mid = (L + R) // 2
        # Route the update query left or right
        if idx <= mid:
            self.update(2 * node, L, mid, idx, char)
        else:
            self.update(2 * node + 1, mid + 1, R, idx, char)
            
        # As the recursion unwinds, recalculate the bridged states upwards
        self.merge(node, L, mid, R)

class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        seg_tree = SegmentTree(s)
        ans = []
        
        for char, idx in zip(queryCharacters, queryIndices):
            # Update the character in O(log N) time
            seg_tree.update(1, 0, len(s) - 1, idx, char)
            
            # The root node (node 1) always holds the global max_len
            ans.append(seg_tree.max_len[1])
            
        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Bridging a gap
    print(f"Test 1: {sol.longestRepeating('babacc', 'bcb', [1, 3, 3])}") 
    # Expected: [3, 3, 4] 
    # (Query 1: "bbbacc" -> max is 3 'b's)
    # (Query 2: "bbbccc" -> max is 3 'b's or 3 'c's)
    # (Query 3: "bbbbcc" -> max is 4 'b's)
    
    # Test 2: Standard progression
    print(f"Test 2: {sol.longestRepeating('abyzz', 'aa', [2, 1])}") 
    # Expected: [2, 3]