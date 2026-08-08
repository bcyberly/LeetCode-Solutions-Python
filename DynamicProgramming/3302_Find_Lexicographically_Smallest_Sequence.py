# Problem: 3302. Find the Lexicographically Smallest Valid Sequence
# Difficulty: Medium
# Link: https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/description

# Time Complexity: O(N) - Where N is the length of word1. The right-to-left suffix generation takes O(N), and the left-to-right greedy matching takes O(N).
# Space Complexity: O(M) - Where M is the length of word2. We store the 'back' array of size M+1 and 'ans' array of size M.

from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)

        # Precompute the "Safety Net" (Right-to-Left Exact Match DP)
        # back[i] sotres the maximum (rightmost) index in word1 such that 
        # the exact suffix word2[i:] can be matched perfectly.
        back = [-1] * (m + 1)
        back[m] = n

        j = n -1
        for i in range(m-1, -1, -1):
            while j >= 0 and word1[j] != word2[i]:
                j-= 1
            if j >= 0:
                back[i] = j
                j -= 1
            else:
                break # Impossible to exactly match the remaining suffix

        # Greedly find the lexicographically smallest sequence (Left-to-Right)
        ans = []
        used_mismatch = False
        j = 0

        for i in range(m):
            found = False

            while j < n:
                if word1[j] == word2[i]:
                    # Exact Match: Unconditionally optimal, we save our mismatch
                    ans.append(j)
                    j += 1
                    found = True
                    break
                elif not used_mismatch and back[i + 1] > j:
                    # Mismatch: Optimal ONLY if the "Safety Net" guarantees
                    # we have enough space to perfectly match the rest of word2
                    ans.append(j)
                    j += 1
                    used_mismatch = True
                    found = True
                    break

                # If neither condition is met, move to the next character in word1
                j += 1

            # If we couldn't find a valid match for word2[i], the sequence is impossible
            if not found:
                return []

        return ans

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Greedy Mismatch is Better than Exact Match!
    print(f"Test 1: {sol.validSequence('bac', 'bc')}") 
    # Expected: [0, 1] 
    # (Matches "ba" with 1 diff. [0, 1] is lexicographically smaller than exact match [0, 2]!)
    
    # Test 2: Impossible Sequence
    print(f"Test 2: {sol.validSequence('aaaaaa', 'abc')}") 
    # Expected: []
    
    # Test 3: Standard Traversal
    print(f"Test 3: {sol.validSequence('abc', 'ab')}") 
    # Expected: [0, 1]