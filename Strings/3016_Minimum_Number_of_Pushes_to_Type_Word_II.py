# Problem: 3016. Minimum Number of Pushes to Type Word II
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/description

# Time Complexity: O(N) - Counting the frequencies takes O(N) time. Sotring the frequency array takes O(1) time because it is strictly bounded to a maximum of 26 elements.
# Space Complexity: O(1) - The Counter or frequency array stores at most 26 key-value pairs, which is constant auxiliary space.

from collections import Counter 

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Count the exact frequency of every letter in the word
        freq = Counter(word)

        # Sort the frquencies in descending order
        # (We only care about the raw counts, not the letters themselves)
        sorted_counts = sorted(freq.values(), reverse=True)

        total_pushes = 0

        # Greedily assign the most frequent letters to the cheapesttiers 
        for i, count in enumerate(sorted_counts):
            # i // 8 gives 0 for the first 8, 1 for the next 8, etc.
            # We add 1 to get the excat cost multiplier (1 push, 2 pushes, 3 pushes...)
            multiplier = (i // 8) + 1

            # Multiply the letter's frquency by its keypad depth cost
            total_pushes += count * multiplier

        return total_pushes

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Distinct letters (Behaves exactly like Part I)
    print(f"Test 1: {sol.minimumPushes('abcde')}") 
    # Expected: 5 (5 letters * 1 push each = 5)
    
    # Test 2: Heavily repeating sub-groups
    print(f"Test 2: {sol.minimumPushes('xyzxyzxyzxyz')}") 
    # Expected: 12 (x:4, y:4, z:4. All top 3 are in Tier 1 -> (4*1)+(4*1)+(4*1) = 12)
    
    # Test 3: Spilling across multiple depth tiers
    print(f"Test 3: {sol.minimumPushes('aabbccddeeffgghhiiiiii')}") 
    # Expected: 24 
    # (i:6, rest:2 each. 'i' and 7 others get Tier 1. The 9th letter 'h' gets Tier 2!)