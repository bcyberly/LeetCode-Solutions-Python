# Problem: 3345. Smallest Divisible Digit Product I
# Difficulty: Easy
# Link: https://leetcode.com/problems/smallest-divisible-digit-product-i/description

# Time Complexity: O(1) - The loop is mathematically guaranteed to run at most 10 times before hitting a number ending in 0 (which yields a digit product of 0, divisible by any t).
# Space Complexity: O(1) - Evaluated entirely in-place with no auxiliary data structures.

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            prod = 1
            
            # Extract digits using modulo arithmetic
            while temp > 0:
                digit = temp % 10
                prod *= digit
                
                # If a digit is 0, the product is 0
                if prod == 0:
                    break
                    
                temp //= 10
                
            # If the product is perfectly divisible by t, we found our answer
            if prod % t == 0:
                return n
                
            n += 1

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: Immediate multiple
    print(f"Test 1: {sol.smallestNumber(10, 2)}") 
    # Expected: 10 (Digits: 1*0 = 0. 0 is divisible by 2)
    
    # Test 2: Standard increment
    print(f"Test 2: {sol.smallestNumber(15, 3)}") 
    # Expected: 16 (1*5 = 5 (No). 1*6 = 6 (Yes, div by 3))
    
    # Test 3: Approaching the Zero-Ceiling
    print(f"Test 3: {sol.smallestNumber(17, 7)}") 
    # Expected: 20 (17, 18, 19 fail. 20 hits 0, which is divisible by 7)