# Problem: 3348. Smallest Divisible Digit Product II
# Difficulty: Hard
# Link: https://leetcode.com/problems/smallest-divisible-digit-product-ii/description

# Time Complexity: O(N) - Precalculating prefix arrays and the backward scan run in linear time. The DP transition matrix resolves in constant time (O(55 * 35)) due to bounding the prime exponents. Fast-forwarding the suffix builds massive strings instantly.
# Space Complexity: O(N) - Allocating prefix arrays (pref2, pref3, pref5, pref7) and the final string array requires memory proportional to the string length N.

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Prime factorize the target 't'
        t2 = t3 = t5 = t7 = 0
        temp = t
        while temp % 2 == 0: t2 += 1; temp //= 2
        while temp % 3 == 0: t3 += 1; temp //= 3
        while temp % 5 == 0: t5 += 1; temp //= 5
        while temp % 7 == 0: t7 += 1; temp //= 7
        
        # If 't' contains prime factors other than 2, 3, 5, or 7, it's impossible to form with digits 1-9
        if temp > 1: return "-1"

        # Predefined prime factor frequencies for digits 0-9
        f2 = [0, 0, 1, 0, 2, 0, 1, 0, 3, 0]
        f3 = [0, 0, 0, 1, 0, 0, 1, 0, 0, 2]
        f5 = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        f7 = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]

        # Build the DP table for transitions involving digits that affect exponents of 2 and 3
        MAX_R2, MAX_R3 = 55, 35
        dp = [[0] * MAX_R3 for _ in range(MAX_R2)]
        digits69 = [2, 3, 4, 6, 8, 9]  # Digits that contribute to factors 2 or 3
        
        for r2 in range(MAX_R2):
            for r3 in range(MAX_R3):
                if r2 == 0 and r3 == 0:
                    continue
                best = float('inf')
                for d in digits69:
                    nr2 = max(0, r2 - f2[d])
                    nr3 = max(0, r3 - f3[d])
                    if nr2 == r2 and nr3 == r3:
                        continue  # Degenerate self-transition — skip, never optimal
                    
                    cand = 1 + dp[nr2][nr3]
                    if cand < best:
                        best = cand
                dp[r2][r3] = best

        N = len(num)
        
        # Precompute prefix sums for the prime factors of the digits in 'num'
        pref2, pref3, pref5, pref7 = [0]*(N+1), [0]*(N+1), [0]*(N+1), [0]*(N+1)
        first_zero = N
        
        for i in range(N):
            d = int(num[i])
            if d == 0 and first_zero == N: 
                first_zero = i
            pref2[i+1] = pref2[i] + f2[d]
            pref3[i+1] = pref3[i] + f3[d]
            pref5[i+1] = pref5[i] + f5[d]
            pref7[i+1] = pref7[i] + f7[d]

        # Helper function to greedily build the lexicographically smallest suffix
        def build_suffix(rem_L, r2, r3, r5, r7):
            res = []
            req = r5 + r7 + dp[r2][r3]
            
            # Pad with '1's if we have more length remaining than required digits (Fast-Forward!)
            if rem_L > req:
                num_ones = rem_L - req
                res.extend(['1'] * num_ones)
                rem_L -= num_ones
                
            # Append the smallest possible valid digits iteratively
            while rem_L > 0:
                for d in range(1, 10):
                    nr2 = max(0, r2 - f2[d])
                    nr3 = max(0, r3 - f3[d])
                    nr5 = max(0, r5 - f5[d])
                    nr7 = max(0, r7 - f7[d])
                    
                    # If this digit allows us to finish within the remaining length, lock it in
                    if nr5 + nr7 + dp[nr2][nr3] <= rem_L - 1:
                        res.append(str(d))
                        r2, r3, r5, r7 = nr2, nr3, nr5, nr7
                        rem_L -= 1
                        break
            return "".join(res)

        # If the original number has no zeros and already satisfies the divisibility condition
        if first_zero == N:
            if pref2[N] >= t2 and pref3[N] >= t3 and pref5[N] >= t5 and pref7[N] >= t7:
                return num

        # Scan backward from the rightmost safe pivot to find the optimal increment point
        for i in range(min(N - 1, first_zero), -1, -1):
            curr_d = int(num[i])
            p2, p3, p5, p7 = pref2[i], pref3[i], pref5[i], pref7[i]
            L = N - 1 - i
            
            # Try to increment the current digit
            for d in range(curr_d + 1, 10):
                r2 = max(0, t2 - p2 - f2[d])
                r3 = max(0, t3 - p3 - f3[d])
                r5 = max(0, t5 - p5 - f5[d])
                r7 = max(0, t7 - p7 - f7[d])
                
                # If valid, construct the prefix, the new digit, and the greedy suffix
                if r5 + r7 + dp[r2][r3] <= L:
                    return num[:i] + str(d) + build_suffix(L, r2, r3, r5, r7)

        # If modifying existing digits is impossible, increase the number's total length
        req_L = t5 + t7 + dp[t2][t3]
        target_len = max(N + 1, req_L)
        return build_suffix(target_len, t2, t3, t5, t7)


# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard heavy computation (The TLE trap solver!)
    print(f"Test 1: {sol.smallestNumber('1234', 256)}") 
    # Expected: "1488"
    
    # Test Case 2: Number with a zero requires modification
    print(f"Test 2: {sol.smallestNumber('10', 2)}") 
    # Expected: "12"
    
    # Test Case 3: Impossible target due to prime factor > 7 (e.g., 11)
    print(f"Test 3: {sol.smallestNumber('123', 11)}") 
    # Expected: "-1"