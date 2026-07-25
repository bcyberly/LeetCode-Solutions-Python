# Problem: 3536. Maximum Product of Two Digits
# Difficulty: Easy
# Link: https://leetcode.com/problems/maximum-product-of-two-digits/description

# Time Complexity: O(d log d) - Where d is the number of digits in n. Since an integer has at most 18-20 digits in standard architectures, this executes in practical O(1) constant time.
# Space Complexity: O(d) - We store the individual digits in an auxiliary list.

class Solution:
    def maxProduct(self, n: int) -> int:
        # Convert the integer to a list of its numerical digits
        digits = [int(char) for char in str(n)]
        
        # Sort descending so the two largest digits sit at index 0 and 1
        digits.sort(reverse=True)
        
        # Multiply the top two largest digits
        return digits[0] * digits[1]

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Standard mix of digits
    print(f"Test 1: {sol.maxProduct(3536)}") 
    # Expected: 30 (Largest digits are 6 and 5 -> 6 * 5 = 30)
    
    # Test 2: Repeated maximum digits
    print(f"Test 2: {sol.maxProduct(992)}") 
    # Expected: 81 (Largest digits are 9 and 9 -> 9 * 9 = 81)
    
    # Test 3: Minimum constraint (two digits)
    print(f"Test 3: {sol.maxProduct(10)}") 
    # Expected: 0 (1 * 0 = 0)