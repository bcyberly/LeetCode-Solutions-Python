# Problem: 3622. Check Divisibility by Digit Sum and Product
# Difficulty: Easy
# Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/description

# Time Complexity: O(log_10(N)) - We extract digits one by one using modulo arithmetic. The number of operations is strictly proportional to the number of digits in N.
# Space Complexity: O(1) - We only allocate a few integer variables (digit_sum, digit_prod, temp) regardless of the size of N.

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        digit_sum = 0
        digit_prod = 1
        
        # Extract digits mathematically without string conversion overhead
        while temp > 0:
            digit = temp % 10
            digit_sum += digit
            digit_prod *= digit
            temp //= 10
            
        # Check if perfectly divisible by the combined total
        return n % (digit_sum + digit_prod) == 0

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1: n = 99 (Expected: True)
    # Sum = 9 + 9 = 18. Prod = 9 * 9 = 81. 
    # Target = 18 + 81 = 99. 
    # 99 % 99 == 0.
    print(f"Test 1 (Number 99):  {sol.checkDivisibility(99)}") 
    
    # Test 2: n = 132 (Expected: True)
    # Sum = 1 + 3 + 2 = 6. Prod = 1 * 3 * 2 = 6. 
    # Target = 6 + 6 = 12. 
    # 132 % 12 == 0.
    print(f"Test 2 (Number 132): {sol.checkDivisibility(132)}")
    
    # Test 3: n = 20 (Expected: True)
    # Any number with a zero has a digit product of 0.
    # Sum = 2 + 0 = 2. Prod = 2 * 0 = 0. 
    # Target = 2 + 0 = 2. 
    # 20 % 2 == 0.
    print(f"Test 3 (Number 20):  {sol.checkDivisibility(20)}")
    
    # Test 4: n = 12 (Expected: False)
    # Sum = 1 + 2 = 3. Prod = 1 * 2 = 2. 
    # Target = 3 + 2 = 5. 
    # 12 % 5 != 0.
    print(f"Test 4 (Number 12):  {sol.checkDivisibility(12)}")