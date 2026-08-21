# LeetCode Solutions in Python

![Problems Solved](https://img.shields.io/badge/Problems%20Solved-153-yellow)
![Python](https://img.shields.io/badge/Python-3.8+-yellow)
![Daily Commits](https://img.shields.io/badge/Daily%20Commits-Yes-brightgreen)
![License](https://img.shields.io/badge/License-MIT-orange)

A curated collection of LeetCode problems solved in Python, with a focus on **clean code**, **optimal approaches**, and **detailed complexity analysis**. Updated daily as part of my commitment to consistent practice.

## 📊 Complexity Legend

| Notation | Meaning | Example |
|----------|---------|---------|
| O(1) | Constant | Hash table lookup / Bitwise ops / Math |
| O(log n) | Logarithmic | Binary search / Single Heap ops |
| O(n) | Linear | Single pass through array/string |
| O(n + m) | Linear Sum | Iterating through two separate inputs |
| O(max(n, m)) | Max Linear | Processing the longer of two inputs |
| O(n log n) | Linearithmic | Efficient sorting / Segment Trees |
| O(n²) | Quadratic | Nested loops / All substrings |
| O(n * m) | Multiplicative | 2D Grid traversal / State-space DP (e.g., O(Z * O)) |
| O(V + E) | Graph Linear | DFS/BFS traversing Vertices and Edges |
| O(E log M) | Graph Logarithmic | Kruskal's Algorithm / Binary Search on Edges |
| O(C(n, k)) | Combinatorial | Backtracking valid combinations |
| O(2^k) | Exponential | All binary combinations of length k |
| O(H) | Tree Height | Space complexity for recursive Call Stack |
| O(U) | Unique Elements | Space complexity for Hash Sets |


## 📁 Repository Structure

LeetCode-Solutions-Python/

├── Arrays/              # 1D Array manipulation & Sliding Window

├── Backtracking/        # Recursive search & Combinations

├── BinarySearch/        # Search space optimization & Math

├── BitManipulation/     # Bitwise operations

├── DynamicProgramming/  # DP & Simulation

├── Graphs/              # DSU, Kruskal's, & Binary Search

├── Math/                # Modular Arithmetic & Number Theory

├── Matrix/              # 2D Grids, Traversals, & Boundary Simulation

├── Strings/             # String processing

├── Trees/               # BST operations & Traversals

└── README.md


## 📚 Solutions by Category

### [Arrays](./Arrays/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 42 | [Trapping Rain Water](./Arrays/0042_Trapping_Rain_Water.py) | Hard | Two Pointers (Min-Max bounds) | O(N) | O(1) |
| 1464 | [Maximum Product of Two Elements in an Array](./Arrays/1464_Maximum_Product_of_Two_Elements.py) | Easy | Dual-Champion Tracking & O(N) Linear Scan | O(N) | O(1) |
| 1536 | [Minimum Swaps to Arrange a Binary Grid](./Arrays/1536_Minimum_Swaps_to_Arrange_a_Binary_Grid.py) | Medium | Greedy (Pop/Insert Simulation) | O(N²) | O(N) |
| 1582 | [Special Positions in a Binary Matrix](./Arrays/1582_Special_Positions_in_a_Binary_Matrix.py) | Easy | Matrix Precomputation | O(M * N) | O(M + N) |
| 1846 | [Maximum Element After Decreasing and Rearranging](./Arrays/1846_Max_Element_After_Decreasing.py) | Medium | Greedy Staircase / O(N) Frequency Buckets | O(N) | O(N) |
| 1848 | [Minimum Distance to the Target Element](./Arrays/1848_Min_Distance_to_Target_Element.py) | Easy | Expanding Window (Early Exit) | O(N) | O(1) |
| 1855 | [Maximum Distance Between a Pair of Values](./Arrays/1855_Max_Distance_Between_Pair.py) | Medium | Two Pointers | O(N+M) | O(1) |
| 1878 | [Get Biggest Three Rhombus Sums in a Grid](./Arrays/1878_Get_Biggest_Three_Rhombus_Sums.py) | Medium | Boundary Simulation | O(M*N*min(M,N)) | O(U) |
| 2078 | [Two Furthest Houses With Different Colors](./Arrays/2078_Two_Furthest_Houses_With_Diff_Colors.py) | Easy | Boundary Anchoring (Two Pointers) | O(N) | O(1) |
| 2144 | [Minimum Cost of Buying Candies With Discount](./Arrays/2144_Min_Cost_Buying_Candies_Discount.py) | Easy | Greedy Descending Sort | O(N log N) | O(1) |
| 2515 | [Shortest Distance to Target String in a Circular Array](./Arrays/2515_Shortest_Distance_Target_String_Circular.py) | Easy | Bidirectional Distance Math | O(N) | O(1) |
| 2574 | [Left and Right Sum Differences](./Arrays/2574_Left_and_Right_Sum_Differences.py) | Easy | Running Prefix & Suffix Sums | O(N) | O(1) |
| 2161 | [Partition Array According to Given Pivot](./Arrays/2161_Partition_Array_According_to_Pivot.py) | Medium | Stable Partition / 3-Bucket Sweep | O(N) | O(N) |
| 2615 | [Sum of Distances](./Arrays/2615_Sum_of_Distances.py) | Medium | Hash Map + Prefix Sums | O(N) | O(N) |
| 2657 | [Find the Prefix Common Array of Two Arrays](./Arrays/2657_Find_the_Prefix_Common_Array.py) | Medium | Shared Frequency Array | O(N) | O(N) |
| 2751 | [Robot Collisions](./Arrays/2751_Robot_Collisions.py) | Hard | Sorting + Stack Simulation | O(N log N) | O(N) |
| 2958 | [Length of Longest Subarray With at Most K Frequency](./Arrays/2958_Length_of_Longest_Subarray_With_at_Most_K_Frequency.py) | Medium | Sliding Window & Frequency Map | O(N) | O(N) |
| 2996 | [Smallest Missing Integer Greater Than Sequential Prefix Sum](./Arrays/2996_Smallest_Missing_Integer_Greater_Than_Sequential_Prefix_Sum.py) | Easy | Greedy Prefix Break & Hash Set Lookup | O(N) | O(N) |
| 3010 | [Divide an Array Into Subarrays With Minimum Cost I](./Arrays/3010_Divide_an_Array_Into_Subbarrays_With_Minimum_Cost_I.py) | Easy | Greedy + Sorting | O(n log n) | O(n) |
| 3013 | [Divide an Array Into Subarrays With Minimum Cost II](./Arrays/3013_Divide_an_Array_Into_Subbarrays_With_Minimum_Cost_II.py) | Hard | Sliding Window + Two Heaps | O(n log d) | O(n) |
| 3020 | [Find the Maximum Number of Elements in Subset](./Arrays/3020_Find_Max_Elements_in_Subset.py) | Medium | Hash Map Frequency & Mountain Pattern Squaring | O(N) | O(N) |
| 3027 | [Find the Number of Ways to Place People II](./Arrays/3027_Find_the_Number_of_Ways_to_Place_People_II.py) | Hard | 2D Geometry Sweep + Running Max | O(N²) | O(1) |
| 3069 | [Distribute Elements Into Two Arrays I](./Arrays/3069_Distribute_Elements_Into_Two_Arrays_I.py) | Easy | Tail Comparison Simulation | O(N) | O(N) |
| 3300 | [Minimum Element After Replacement With Digit Sum](./Arrays/3300_Min_Element_After_Replacement_Digit_Sum.py) | Easy | Linear Scan + Modulo Digit Extraction | O(N) | O(1) |
| 3379 | [Transformed Array](./Arrays/3379_Transformed_Array.py) | Easy | Simulation (Modular Arithmetic) | O(n) | O(n) |
| 3471 | [Find the Largest Almost Missing Integer](./Arrays/3471_Largest_Almost_Missing_Integer.py) | Easy | Sliding Window Set Sieve | O(N \times K) | O(N) |
| 3488 | [Closest Equal Element Queries](./Arrays/3488_Closest_Equal_Element_Queries.py) | Medium | Hash Map + Circular Math | O(N + Q) | O(N) |
| 3633 | [Earliest Finish Time for Land and Water Rides I](./Arrays/3633_Earliest_Finish_Time_Land_Water_Rides_I.py) | Easy | Simulation / Min-Max Bounding | O(N*M) | O(1) |
| 3634 | [Minimum Removals to Balance Array](./Arrays/3634_Minimum_Removals_to_Balance.py) | Medium | Two Pointers + Sorting | O(n log n) | O(1) |
| 3637 | [Trionic Array I](./Arrays/3637_Trionic_Array_I.py) | Easy | Linear Scan (Pattern Recognition) | O(n) | O(1) |
| 3640 | [Trionic Array II](./Arrays/3640_Trionic_Array_II.py) | Hard | Dynamic Programming (State Machine) | O(n) | O(n) |
| 3653 | [XOR After Range Multiplication Queries I](./Arrays/3653_XOR_After_Range_Multiplication_I.py) | Medium | Array Simulation | O(Q*N) | O(1) |
| 3655 | [XOR After Range Multiplication Queries II](./Arrays/3655_XOR_After_Range_Multiplication.py) | Hard | Sqrt Decomposition / Difference Arrays | O(N * sqrt(Q)) | O(N) |
| 3660 | [Jump Game IX](./Arrays/3660_Jump_Game_IX.py) | Medium | Prefix Max & Suffix Min Sweeps | O(N) | O(N) |
| 3719 | [Longest Balanced Subarray I](./Arrays/3719_Longest_Balanced_Subarray_I.py) | Medium | Brute Force (All Subarrays)| O(n²) | O(n) |
| 3721 | [Longest Balanced Subarray II](./Arrays/3721_Longest_Balanced_Subarray_II.py) | Hard | Segment Tree + Prefix Sums | O(n log n) | O(n) |
| 3731 | [Find Missing Elements](./Arrays/3731_Find_Missing_Elements.py) | Easy | Hash Set Range Sweep | O(N+R) | O(N) |
| 3737 | [Count Subarrays With Majority Element I](./Arrays/3737_Count_Subarrays_With_Majority_Element_I.py) | Medium | +1/-1 Transformation & Rolling Prefix Balance | O(N) | O(N) |
| 3739 | [Count Subarrays With Majority Element II](./Arrays/3739_Count_Subarrays_With_Majority_Element_II.py) | Hard | +1/-1 Transformation & Rolling Prefix Balance | O(N) | O(N) |
| 3740 | [Minimum Distance Between Three Equal Elements I](./Arrays/3740_Min_Dist_Three_Equal_Elements_I.py) | Easy | Hash Map + Index Tracking | O(N) | O(N) |
| 3741 | [Minimum Distance Between Three Equal Elements II](./Arrays/3741_Min_Dist_Three_Equal_Elements_II.py) | Medium | Hash Map + Index Tracking | O(N) | O(N) |
| 3761 | [Minimum Absolute Distance Between Mirror Pairs](./Arrays/3761_Min_Abs_Distance_Mirror_Pairs.py) | Medium | Hash Map + Index Tracking | O(N) | O(N) |

### [Strings](./Strings/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 67 | [Add Binary](./Strings/0067_Add_Binary.py) | Easy | Bit Manipulation (Simulation) | O(n + m) | O(max(n,m)) |
| 696 | [Count Binary Substrings](./Strings/0696_Count_Binary_Substrings.py) | Easy | Linear Scan (Group Counting) | O(n) |	O(1) |
| 761 | [Special Binary String](./Strings/0761_Special_Binary_String.py) | Hard | Recursion + Sorting | O(n²) | O(n) |
| 1081 | [Smallest Subsequence of Distinct Characters](./Strings/1081_Smallest_Subsequence_Distinct.py) | Medium | Monotonic Stack & Last Occurrence Tracker | O(N) | O(1) |
| 1189 | [Maximum Number of Balloons](./Strings/1189_Maximum_Number_of_Balloons.py) | Easy | Hash Map Frequency Counting | O(N) | O(1) |
| 1291 | [Sequential Digits](./Strings/1291_Sequential_Digits.py) | Medium | Master String Sliding Window | O(1) | O(1) |
| 1358 | [Number of Substrings Containing All Three Characters](./Strings/1358_Number_of_Substrings_Containing_All_Three.py) | Medium | Sliding Window / Last-Seen Index Tracking | O(N) | O(1) |
| 1461 | [Check If a String Contains All Binary Codes](./Strings/1461_Check_If_String_Contains_All_Binary_Codes.py) | Medium | Sliding Window Set / Rolling Hash | O(N) | O(N*K) |
| 1545 | [Find Kth Bit in Nth Binary String](./Strings/1545_Find_Kth_Bit_in_Nth_Binary_String.py) | Medium | Divide & Conquer (Recursion) | O(N) | O(N) |
| 1689 | [Partitioning Into Minimum Number Of Deci-Binary Numbers](./Strings/1689_Partitioning_into_Minimum_number_Of_Deci-Binary_Numbers.py) | Medium | Greedy (Max Digit Search) | O(n) | O(1) |
| 1758 | [Minimum Changes To Make Alternating Binary String](./Strings/1758_Minimum_Changes_To_Make_Alternating_Binary_String.py) | Easy | Symmetric Pattern Counting | O(n) | O(1) |
| 1784 | [Check if Binary String Has at Most One Segment of Ones](./Strings/1784_Check_if_Binary_String_Has_at_Most_One_Segment_of_Ones.py) | Easy | Linear Scan State Tracking | O(n) | O(1) |
| 1888 | [Minimum Number of Flips to Make the Binary String Alternating](./Strings/1888_Minimum_Number_of_Flips_to_Make_the_Binary_String_Alternating.py) | Medium | Sliding Window (Virtual Doubling) | O(N) | O(1) |
| 1967 | [Number of Strings That Appear as Substrings in Word](./Strings/1967_Num_Strings_Appear_as_Substrings.py) | Easy | Built-in Substring Search | O(P*N) | O(1) |
| 1980 | [Find Unique Binary String](./Strings/1980_Find_Unique_Binary_String.py) | Medium | Cantor's Diagonalization | O(N) | O(N) |
| 2452 | [Words Within Two Edits of Dictionary](./Strings/2452_Words_Within_Two_Edits.py) | Medium | Hamming Distance / Early Exit | O(Q*D*L) | O(1) |
| 2573 | [Find the String with LCP](./Strings/2573_Find_the_String_with_LCP.py) | Hard | Greedy Assignment / DP Validation | O(N²) | O(N) |
| 2833 | [Furthest Point From Origin](./Strings/2833_Furthest_Point_From_Origin.py) | Easy | Greedy / Counting | O(N) | O(1) |
| 2839 | [Check if Strings Can be Made Equal With Operations I](./Strings/2839_Check_if_Strings_Can_be_Made_Equal.py) | Easy | Parity Grouping + Sorting | O(1) | O(1) |
| 2840 | [Check if Strings Can be Made Equal With Operations II](./Strings/2840_Check_if_Strings_Can_be_Made_Equal_II.py) | Medium | Parity Grouping + Frequency Map | O(N) | O(1) |
| 3014 | [Minimum Number of Pushes to Type Word I](./Strings/3014_Minimum_Number_of_Pushes_to_Type_Word_I.py) | Easy | Greedy Tier Allocation & String Length | O(1) | O(1) |
| 3016 | [Minimum Number of Pushes to Type Word II](./Strings/3016_Minimum_Number_of_Pushes_to_Type_Word_II.py) | Medium | Greedy Frequency Tier Allocation & 26-Array Sieve | O(N) | O(1) |
| 3090 | [Maximum Length Substring With Two Occurrences](./Strings/3090_Maximum_Length_Substring_With_Two_Occurrences.py) | Easy | Sliding Window Frequency Bounding | O(N) | O(1) |
| 3501 | [Maximize Active Section with Trade II](./Strings/3501_Maximize_Active_Section_Trade_II.py) | Hard | Sparse Table (RMQ) & Block Parsing | O(NlogN+QlogM) | O(NlogN) |
| 3517 | [Smallest Palindromic Rearrangement I](./Strings/3517_Smallest_Palindromic_Rearrangement_I.py) | Medium | Alphabetical Frequency Half-Build & Mirroring | O(N) | O(N) |
| 3518 | [Smallest Palindromic Rearrangement II](./Strings/3518_Smallest_Palindromic_Rearrangement_II.py) | Hard | Combinatorial Prefix Skipping | O(N) | O(N) |
| 3532 | [Path Existence Queries in a Graph I](./Graphs/3532_Path_Existence_Queries_in_a_Graph_I.py) | Medium | Sorted Contiguous Component Labeling | O(N+Q) | O(N) |
| 3474 | [Lexicographically Smallest Generated String](./Strings/3474_Lexicographically_Smallest_Generated.py) | Hard | KMP Automaton / Backtracking | O(N+M) | O(N+M) |
| 3499 | [Maximize Active Section with Trade I](./Strings/3499_Maximize_Active_Section_Trade.py) | Medium | itertools.groupby & The 1-Refund Illusion | O(N) | O(N) |
| 3713 | [Longest Balanced Substring I](./Strings/3713_Longest_Balanced_Substring_I.py) | Medium | Brute Force (All Substrings) | O(n²) | O(1) |
| 3714 | [Longest Balanced Substring II](./Strings/3714_Longest_Balanced_Substring_II.py) | Medium | Prefix Difference Map | O(n) | O(n) |
| 3756 | [Concatenate Non-Zero Digits and Multiply by Sum II](./Strings/3756_Concatenate_Non_Zero_Digits_II.py) | Medium | Non-Zero Compression & Prefix Math | O(M+QlogM) | O(M) |

### [Backtracking](./Backtracking/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 37 | [Sudoku Solver](./Backtracking/0037_Sudoku_Solver.py) | Hard | Backtracking (Hash Set Pruning) | O(9^(Empty)) | O(1) |
| 401 | [Binary Watch](./Backtracking/0401_Binary_Watch.py) | Easy | Backtracking / Bit Counting | O(C(10, k)) | O(k) |
| 1415 | [The k-th Lexicographical String of All Happy Strings of Length n](./Backtracking/1415_The_kth_Lexicographical_String_of_All_Happy_Strings.py) | Medium | Combinatorial Math / Decision Tree | O(N) | O(N) |

### [BinarySearch](./BinarySearch/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 3116 | [Kth Smallest Amount With Single Denomination Combination](./BinarySearch/3116_Kth_Smallest_Amount.py) | Hard | Binary Search on Answer & Inclusion-Exclusion (PIE) | O(2^N \log M) | O(2^N) |
| 3296 | [Minimum Number of Seconds to Make Mountain Height Zero](./BinarySearch/3296_Min_Seconds_Mountain_Zero.py) | Medium | Binary Search on Answer + Quadratic Formula | O(N log M) | O(1) |
| 3464 | [Maximize the Distance Between Points on a Square](./BinarySearch/3464_Maximize_Distance_Square.py) | Hard | 1D Mapping / Binary Search on Answer | O(N log N) | O(N) |
| 3635 | [Earliest Finish Time for Land and Water Rides II](./BinarySearch/3635_Earliest_Finish_Time_Land_Water_Rides_II.py) | Medium | Binary Search / Prefix & Suffix Sweeps | O(NlogN + MlogM) | O(N+M) |

### [BitManipulation](./BitManipulation/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 190 | [Reverse Bits](./BitManipulation/0190_Reverse_Bits.py) | Easy | Divide & Conquer (Bitwise Merge) | O(1) | O(1) |
| 693 | [Binary Number with Alternating Bits](./BitManipulation/0693_Binary_Number_with_Alternating_Bits.py) | Easy | Bit Manipulation (XOR & Check) | O(1) | O(1) |
| 762 | [Prime Number of Set Bits in Binary Representation](./BitManipulation/0762_Prime_Number_of_Set_Bits_in_Binary_Representation.py) | Easy | Bit Manipulation + Fast Prime Set | O(n) | O(1) |
| 868 | [Binary Gap](./BitManipulation/0868_Binary_Gap.py) | Easy | Bitwise Shift & Masking | O(log n) | O(1) |
| 1009 | [Complement of Base 10 Integer](./BitManipulation/1009_Complement_of_Base_10_Integer.py) | Easy | Bitmask & XOR | O(1) | O(1) |
| 1356 | [Sort Integers by The Number of 1 Bits](./BitManipulation/1356_Sort_Integers_by_The_Number_of_1_Bits.py) | Easy | Custom Sort & Bit Count | O(N log N) | O(1) |
| 1386 | [Cinema Seat Allocation](./BitManipulation/1386_Cinema_Seat_Allocation.py) | Medium | Hash Map & Bitmask Overlap Deduction | O(M) | O(M) |
| 1404 | [Number of Steps to Reduce a Number in Binary Representation to One](./BitManipulation/1404_Number_of_Steps_to_Reduce_a_Number_in_Binary_Representation_to_One.py) | Medium | Right-to-Left Carry Tracking | O(N) | O(1) |
| 1680 | [Concatenation of Consecutive Binary Numbers](./BitManipulation/1680_Concatenation_of_Consecutive_Binary_Numbers.py) | Medium | Bitwise Shift & Modulo | O(N) | O(1) |
| 3513 | [Number of Unique XOR Triplets I](./BitManipulation/3513_Number_of_Unique_XOR_Triplets_I.py) | Medium | O(1) Bit-Length Vector Span | O(1) | O(1) |
| 3514 | [Number of Unique XOR Triplets II](./BitManipulation/3514_Number_of_Unique_XOR_Triplets_II.py) | Medium | 2-Step Pairwise XOR Sieve & Boolean Array Optimization | O(U^2+P*U) | O(U+P+V) |
| 3666 | [Minimum Operations to Equalize Binary String](./BitManipulation/3666_Minimum_Operations_to_Equalize_Binary_String.py) | Hard | SortedList BFS Parity Search | O(N log N) | O(N) |
| 3702 | [Longest Subsequence With Non-Zero Bitwise XOR](./BitManipulation/3702_Longest_Subsequence_With_Non_Zero_Bitwise_XOR.py) | Medium | Global XOR & Single Element Exclusion | O(N) | O(1) |

### [DynamicProgramming](./DynamicProgramming/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 486 | [Predict the Winner](./DynamicProgramming/0486_Predict_the_Winner.py) | Medium | Minimax DP Net-Difference Relation & 1D Space Optimization | O(N^2) | O(N) |
| 799 | [Champagne Tower](./DynamicProgramming/0799_Champagne_Tower.py) | Medium | Simulation + DP (In-place) | O(R²) | O(R) |
| 1140 | [Stone Game II](./DynamicProgramming/1140_Stone_Game_II.py) | Medium | Minimax DP & Suffix Sum Optimization | O(N³) | O(N²) |
| 1320 | [Minimum Distance to Type a Word Using Two Fingers](./DynamicProgramming/1320_Min_Distance_Type_Word_Two_Fingers.py) | Hard | Top-Down DP (State Compression) | O(N) | O(N) |
| 1340 | [Jump Game V](./DynamicProgramming/1340_Jump_Game_V.py) | Hard | Top-Down DP (Memoization) / DAG Traversal | O(N*d) | O(N) |
| 1406 | [Stone Game III](./DynamicProgramming/1406_Stone_Game_III.py) | Hard | Minimax Net-Difference DP & O(1) Sliding Window | O(N) | O(1) |
| 1510 | [Stone Game IV](./DynamicProgramming/1510_Stone_Game_IV.py) | Hard | Win-State DP & Square Root Bounding | O(N\sqrt{N}) | O(N) |
| 1563 | [Stone Game V](./DynamicProgramming/1563_Stone_Game_V.py) | Hard | Divide & Conquer DP with Prefix Sums | O(N³) | O(N²) |
| 1594 | [Maximum Non Negative Product in a Matrix](./DynamicProgramming/1594_Max_Non_Negative_Product_Matrix.py) | Medium | 2D DP (Min/Max Dual-State) | O(M*N) | O(M*N) |
| 1871 | [Jump Game VII](./DynamicProgramming/1871_Jump_Game_VII.py) | Medium | 1D DP + Sliding Window Count | O(N) | O(N) |
| 2463 | [Minimum Total Distance Traveled](./DynamicProgramming/2463_Min_Total_Distance_Traveled.py) | Hard | Top-Down DP (Capacity Batching) | O(R² * F) | O(R * F) |
| 2946 | [Matrix Similarity After Cyclic Shifts](./Matrix/2946_Matrix_Similarity_After_Cyclic_Shifts.py) | Easy | Modular Arithmetic + Slice Comparison | O(M*N) | O(N) |
| 3129 | [Find All Possible Stable Binary Arrays I](./DynamicProgramming/3129_Find_All_Possible_Stable_Binary_Arrays_I.py) | Medium | DP with Invalid State Subtraction | O(Z * O) | O(Z * O) |
| 3130 | [Find All Possible Stable Binary Arrays II](./DynamicProgramming/3130_Find_All_Possible_Stable_Binary_Arrays_II.py) | Hard | DP with Invalid State Subtraction | O(Z * O) | O(Z * O) |
| 3225 | [Maximum Score From Grid Operations](./DynamicProgramming/3225_Max_Score_Grid_Operations.py) | Hard | DP (State Decoupling) + Prefix Sums | O(N³) | O(N²) |
| 3302 | [Find the Lexicographically Smallest Valid Sequence](./DynamicProgramming/3302_Find_Lexicographically_Smallest_Sequence.py) | Medium | Right-to-Left Prefix Suffix DP & Greedy Selection | O(N) | O(M) |
| 3418 | [Maximum Amount of Money Robot Can Earn](./DynamicProgramming/3418_Max_Money_Robot_Can_Earn.py) | Medium | 3D DP (State Tracking) | O(M*N) | O(M*N) |
| 3661 | [Maximum Walls Destroyed by Robots](./DynamicProgramming/3661_Max_Walls_Destroyed_Robots.py) | Hard | Bounded Intervals + 1D DP | O(R log R + W log W) | O(R + W) |
| 3699 | [Number of ZigZag Arrays I](./DynamicProgramming/3699_Number_of_ZigZag_Arrays_I.py) | Hard | Directional DP + Prefix/Suffix Sum Sweeps | O(N*K) | O(K) |
| 3700 | [Number of ZigZag Arrays II](./DynamicProgramming/3700_Number_of_ZigZag_Arrays_II.py) | Hard | Block Matrix Exponentiation | O(M³logN) | O(M²) |
| 3751 | [Total Waviness of Numbers in Range I](./DynamicProgramming/3751_Total_Waviness_of_Numbers_in_Range_I.py) | Medium | Digit DP / Prefix State Tracking | O(log N) | O(log N) |
| 3753 | [Total Waviness of Numbers in Range II](./DynamicProgramming/3753_Total_Waviness_of_Numbers_in_Range_II.py) | Hard | Digit DP / Prefix State Tracking | O(log N) | O(log N) |

### [Trees](./Trees/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1022 | [Sum of Root To Leaf Binary Numbers](./Trees/1022_Sum_of_Root_To_Leaf_Binary_Numbers.py) | Easy | DFS & Bitwise Shift | O(N) | O(H) |
| 1382 | [Balance a Binary Search Tree](./Trees/1382_Balance_a_Binary_Search_Tree.py) | Medium | In-Order Traversal + Divide & Conquer | O(n) | O(n) |
| 2213 | [Longest Substring of One Repeating Character](./Trees/2213_Longest_Substring_of_One_Repeating_Character.py) | Hard | Segment Tree Boundary Merging | O(N+K\log N) | O(N) |
| 2196 | [Create Binary Tree From Descriptions](./Trees/2196_Create_Binary_Tree_From_Descriptions.py) | Medium | Hash Map + Set (Root Identification) | O(N) | O(N) |
| 3558 | [Number of Ways to Assign Edge Weights I](./Trees/3558_Num_Ways_Assign_Edge_Weights_I.py) | Medium | BFS Depth Traversal + Combinatorics | O(N) | O(N) |

### [Graphs](./Graphs/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 1391 | [Check if There is a Valid Path in a Grid](./Graphs/1391_Valid_Path_in_Grid.py) | Medium | BFS / Grid Traversal | O(M*N) | O(M*N) |
| 1559 | [Detect Cycles in 2D Grid](./Graphs/1559_Detect_Cycles_in_2D_Grid.py) | Medium | BFS / Cycle Detection | O(M*N) | O(M*N) |
| 1722 | [Minimize Hamming Distance After Swap Operations](./Graphs/1722_Min_Hamming_Distance_Swaps.py) | Medium | Union-Find / Connected Components | O(N) | O(N) |
| 3310 | [Remove Methods From Project](./Graphs/3310_Remove_Methods_From_Project.py) | Medium | Two-Phase BFS Infection & Isolation Check | O(V+E) | O(V+E) |
| 3600 | [Maximize Spanning Tree Stability with Upgrades](./Graphs/3600._Maximize_Spanning_Tree_Stability_with_Uprades.py) | Hard | Binary Search on Answer + Kruskal's (DSU) | O(E log M) | O(V + E) |


### [Math](./Math/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 628 | [Maximum Product of Three Numbers](./Math/0628_Maximum_Product_of_Three_Numbers.py) | Easy | Dual-Extreme Comparison & O(N) Single-Pass Scan | O(N) | O(1) |
| 1622 | [Fancy Sequence](./Math/1622_Fancy_Sequence.py) | Hard | Modular Inverse (Fermat's Little Theorem) | O(1)* | O(N) |
| 877 | [Stone Game](./Math/0877_Stone_Game.py) | Medium | Game Theory Parity Strategy | O(1) | O(1) |
| 1979 | [Find Greatest Common Divisor of Array](./Math/1979_Find_Greatest_Common_Divisor_of_Array.py) | Easy | O(N) Min-Max Scan & Euclidean Algorithm | O(N) | O(1) |
| 2029 | [Stone Game IX](./Math/2029_Stone_Game_IX.py) | Medium | Modulo 3 Frequency Buckets & Parity Logic | O(N) | O(1) |
| 2033 | [Minimum Operations to Make a Uni-Value Grid](./Math/2033_Min_Operations_Uni_Value_Grid.py) | Medium | Median Minimization / Modulo Math | O(N log N) | O(N) |
| 3312 | [Sorted GCD Pair Queries](./Math/3312_Sorted_GCD_Pair_Queries.py) | Hard | Inclusion-Exclusion Sieve & Prefix Binary Search | O(M log M) | O(M) |
| 3345 | [Smallest Divisible Digit Product I](./Math/3345_Smallest_Divisible_Digit_Product_I.py) | Easy | Modulo Arithmetic & Zero-Digit Ceiling | O(1) | O(1) |
| 3348 | [Smallest Divisible Digit Product II](./Math/3348_Smallest_Divisible_Digit_Product_II.py) | Hard | Prime Factor DP & Fast-Forward Suffix Generation | O(N) | O(N) |
| 3536 | [Maximum Product of Two Digits](./Math/3536_Maximum_Product_of_Two_Digits.py) | Easy | Top-Two Digit Extraction & Modulo Arithmetic | O(d) | O(1) |
| 3658 | [GCD of Odd and Even Sums](./Math/3658_GCD_of_Odd_and_Even_Sums.py) | Easy | Mathematical Simplification | O(1) | O(1) |
| 3754 | [Concatenate Non-Zero Digits and Multiply by Sum I](./Math/3754_Concatenate_Non_Zero_Digits_and_Multiply_by_Sum_I.py) | Easy | String Filtering & Digit Sum Math | O(D) | O(D) |
| 3783 | [Mirror Distance of an Integer](./Math/3783_Mirror_Distance_of_an_Integer.py) | Easy | String Slicing / Digit Extraction | O(D) | O(D) |
| 3867 | [Sum of GCD of Formed Pairs](./Math/3867_Sum_of_GCD_of_Formed_Pairs.py) | Medium | In-Place Prefix Computation & Two Pointers | O(N log N) | O(1) |

### [Matrix](./Matrix/)

| # | Problem | Difficulty | Approach | Time | Space |
|---|---------|------------|----------|------|-------|
| 36 | [Valid Sudoku](./Matrix/0036_Valid_Sudoku.py) | Medium | Matrix Traversal / Hash Set Validation | O(1) | O(1) |
| 212 | [Word Search II](./Matrix/0212_Word_Search_II.py) | Hard | Trie (Prefix Tree) + DFS Backtracking | O(M*N*3^L) | O(W) |
| 1260 | [Shift 2D Grid](./Matrix/1260_Shift_2D_Grid.py) | Easy | 1D Flattening & Inverse Modulo Math | O(M*N) | O(M*N) |
| 1727 | [Largest Submatrix With Rearrangements](./Matrix/1727_Largest_Submatrix_With_Rearrangements.py) | Medium | Histogram Heights + Greedy Sorting | O(M * N log N) | O(1) |
| 1886 | [Determine Whether Matrix Can Be Obtained By Rotation](./Matrix/1886_Determine_Whether_Matrix_Can_Be_Obtained_By_Rotation.py) | Easy | In-Place Transpose + Reverse | O(N²) | O(1) |
| 2812 | [Find the Safest Path in a Grid](./Matrix/2812_Find_the_Safest_Path_in_a_Grid.py) | Medium | Multi-Source BFS & Max-Heap | O(N²logN) | O(N²) |
| 2906 | [Construct Product Matrix](./Matrix/2906_Construct_Product_Matrix.py) | Medium | Prefix & Suffix Sweeps | O(N*M) | O(1)* |
| 3070 | [Count Submatrices with Top-Left Element and Sum Less Than k](./Matrix/3070_Count_Submatrices_Top_Left.py) | Medium | 2D Prefix Sum + Staircase Pruning | O(M*N) | O(1) |
| 3212 | [Count Submatrices With Equal Frequency of X and Y](./Matrix/3212_Count_Submatrices_Equal_Frequency.py) | Medium | Space-Optimized 2D Prefix Sum | O(M*N) | O(N) |
| 3546 | [Equal Sum Grid Partition I](./Matrix/3546_Equal_Sum_Grid_Partition_I.py) | Medium | 1D Spatial Projection + Prefix Sum | O(M*N) | O(M+N) |
| 3567 | [Minimum Absolute Difference in Sliding Submatrix](./Matrix/3567_Min_Abs_Difference_Sliding_Submatrix.py) | Medium | Submatrix Extraction + Sorting | O(M*N*K²logK) | O(K²) |
| 3548 | [Equal Sum Grid Partition II](./Matrix/3548_Equal_Sum_Grid_Partition_II.py) | Hard | Topological Connectivity + Dynamic Maps | O(M*N) | O(M*N) |
| 3643 | [Flip Square Submatrix Vertically](./Matrix/3643_Flip_Square_Submatrix_Vertically.py) | Easy | Two-Pointer Slice Swap | O(K²) | O(K) |

## 🎯 Problem Solving Approach

Each solution file follows a consistent structure to ensure readability and maintainability:

```python
# Problem: [Problem Name]
# Difficulty: [Difficulty Level]
# Link: [LeetCode Link]

# Time Complexity: O(?) - [Explanation of the dominant operation]
# Space Complexity: O(?) - [Explanation of auxiliary space used]

class Solution:
    def method_name(self, ...):
        # Implementation with clear comments holding the logic
        pass

# ---------------------------------------------------
# Local Test Area
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    print(solution.method_name(...))
```

## 📈 Progress Tracker
Total Problems: 153

Easy: 46

Medium: 71

Hard: 36 

Last updated: Daily  

---

# 💡 Algorithm Technique Map

| Core Category              | Problems |
|----------------------------|----------|
| Greedy / Sorting           | 1536, 1689, 1727, 1846, 2144, 2833, 3010, 3016, 3634 |
| Sliding Window             | 42, 1358, 1461, 1848, 1871, 2958, 3090, 3302, 3471 |
| Bit Manipulation           | 67, 190, 401, 693, 762, 868, 1009, 1356, 1386, 1404, 1680, 1855, 3666 |
| DFS / Trees                | 212, 1022, 1382, 2196 |
| Dynamic Programming        | 486, 799, 1140, 1320, 1340, 1406, 1563, 1594, 1510, 2463, 2573, 2574, 3129, 3130, 3225, 3418, 3640, 3700, 3751, 3753 |
| Prefix / Range Queries     | 2906, 3070, 3212, 3546, 3635, 3660, 3714, 3721, 3737, 3739, 3756 |
| Simulation / Linear Scan   | 696, 1291, 1582, 1758, 1784, 1878,1967, 1980, 2161, 2996, 3014, 3069, 3379, 3499, 3517, 3633, 3637 |
| Brute Force / Recursion    | 761, 1545, 3713, 3719 |
| Graphs    | 1391, 1559, 2812, 3310, 3532, 3600 |
| Binary Search on Answer    |  3116, 3296, 3464, 3600 |
| Backtracking / Decision Tree | 37, 401, 1415 |
| Math / Modular Arithmetic  | 628, 877, 1464, 1622, 1979, 2029, 2033, 3300, 3312, 3345, 3348, 3518, 3536, 3558, 3658, 3754, 3783, 3867 |
| Matrix / 2D Traversal      | 1260, 1582, 1594, 1727, 1878, 1886, 2906, 2946, 3070, 3212, 3546, 3548, 3567, 3643 |
| String Manipulation / Parity | 2451, 2839, 2840 |
| Arrays / Circular Traversal | 2515 |
| Hash Map / Index Tracking | 36, 1189, 2615, 2657, 3020, 3488, 3731, 3740, 3741, 3761 |
| Union-Find / Disjoint Set | 1722 |
| Square Root Decomposition / Chunking | 3655 |
| Array Simulation | 3653 |
| Interval Sweeping / Bounded States | 3661 |
| String Matching / KMP Automaton | 3474 |
| Stack / 1D Simulation | 1081, 2751 |
| Geometric Sweeping / Running Max | 3027 |
| Segment Tree / Fenwick / RMQ | 307, 315, 2213, 2407, 3183, 3501, 3688 |
| Bit Manipulation / XOR     | 453, 3513, 3514, 3702 |

## 📝 Solution Highlights

### Efficient Implementations

**67. Add Binary**: Simulates a hardware adder using XOR and AND operations, handling carry-overs efficiently.  

**696. Count Binary Substrings**: Uses a single pass to group consecutive identical characters, then sums the minimum of adjacent group lengths - an O(n) time, O(1) space solution.

**3714. Longest Balanced Substring II**: Optimizes a string problem from O(n²) to O(n) by tracking prefix differences in a hash map.  

**401. Binary Watch**: Uses backtracking with pruning to explore only valid time combinations, avoiding unnecessary checks.  

**693. Binary Number with Alternating Bits**: Uses a clever bitwise trick: XOR the number with its right shift; if the result is all ones, the bits alternate. Then checks if (x & (x + 1)) == 0 to confirm all bits are set.

**Brute Force Approaches 3713. Longest Balanced Substring I & 3719. Longest Balanced Subarray I**: Both demonstrate straightforward brute‑force solutions by checking all substrings/subarrays. While not optimal, they serve as clear baselines and illustrate the problem constraints.

**762. Prime Number of Set Bits**: Leverages Python's highly optimized `.bit_count()` method and a hardcoded O(1) lookup set for primes up to 20, avoiding complex math checks on the fly and keeping the solution blazing fast.

**1461. Check If a String Contains All Binary Codes**: Showcases the progression from a standard O(N*K) sliding window Hash Set to a bare-metal O(2^K) Rolling Hash. By using bitwise shifts to update the window and a `bytearray` as a boolean checklist, it reduces a potential 100MB string allocation down to a 1MB footprint.


**1758. Minimum Changes To Make Alternating Binary String**: Avoids simulating both possible alternating string patterns by using mathematical symmetry: if Pattern A requires `x` flips, Pattern B mathematically requires exactly `N - x` flips. 

**1689. Partitioning Into Minimum Number Of Deci-Binary Numbers**: Reduces a seemingly complex dynamic programming problem into a pure $O(N)$ Greedy scan by realizing the number of required deci-binary layers is simply equal to the maximum single digit found within the string.

**3643. Flip Square Submatrix Vertically**: Showcases idiomatic Python by utilizing slice assignment (`grid[top][y:y+k], grid[bottom][y:y+k] = ...`) combined with a two-pointer approach to reverse a targeted submatrix in-place, keeping the codebase extremely clean and avoiding the boilerplate of nested element-wise swapping loops.

**1886. Determine Whether Matrix Can Be Obtained By Rotation**: Avoids complex coordinate mapping by breaking a 90-degree matrix rotation into two primitive $O(1)$ space operations: a diagonal transposition followed by a horizontal row reversal. This allows for rapid, in-place orientation checks without allocating memory for rotated copies.

**2946. Matrix Similarity After Cyclic Shifts**: Bypasses the Time Limit Exceeded (TLE) trap of simulating massive shift constraints by utilizing Modular Arithmetic (`k % n`). To achieve strict $O(1)$ auxiliary space, it abandons array reallocation entirely, instead mapping cyclical coordinate geometry to dynamically verify if an element `k` steps away matches the current index.

**36. Valid Sudoku**: Replaces the inefficient $O(N^3)$ approach of rescanning rows and columns with a single $O(1)$ pass. Utilizes three arrays of Hash Sets to record seen values in real-time, leveraging mathematical integer division `(r // 3) * 3 + (c // 3)` to instantly map 2D coordinates to their corresponding $3 \times 3$ sub-box.

**212. Word Search II**: Bypasses the catastrophic Time Limit Exceeded (TLE) of running $K$ individual DFS searches by utilizing a Trie (Prefix Tree). The DFS traverses the grid and the Trie simultaneously, instantly pruning paths that do not form a valid prefix for any word in the dictionary. Implements dynamic node deletion upon word discovery to further prevent redundant recursive traversals.

**2657. Find the Prefix Common Array of Two Arrays**: Avoids an $O(N^2)$ nested prefix comparison by leveraging the mathematical properties of permutations. Uses a single shared frequency array to track elements as they are revealed; whenever an element's frequency hits exactly 2, it is guaranteed to have appeared in both arrays, allowing for an optimal $O(N)$ real-time sweep.

**3660. Jump Game IX**: Avoids the $O(N^2)$ trap of simulating graph reachability by mathematically analyzing the global landscape. It uses a dual-sweep approach: a left-to-right Prefix Max sweep to determine local capacity, and a right-to-left Suffix Min sweep. If a point's Prefix Max exceeds the Suffix Min ahead of it, it successfully bridges into the right-side network, resolving the entire array in a strictly linear $O(N)$ pass.

**3300. Minimum Element After Replacement With Digit Sum**: Avoids the performance overhead of casting integers to strings (`str(num)`) by utilizing pure base-10 mathematics. Extracts and sums individual digits in-place using a `num % 10` modulo operation and a `num //= 10` reduction, keeping the auxiliary space strictly $O(1)$ and minimizing memory allocations during the linear scan.

**2144. Minimum Cost of Buying Candies With Discount**: Demonstrates a classic Greedy optimization. By sorting the array in descending order, the algorithm forces the "free" items to be as expensive as mathematically possible. It then computes the minimum total cost in a single pass by exploiting a modulo check (`i % 3 != 2`) to effortlessly skip the cost of every third item.

**3633. Earliest Finish Time for Land and Water Rides I**: Uses a straightforward $O(N \times M)$ simulation to test both chronological permutations (Land-then-Water vs. Water-then-Land) for every possible ride pairing. Employs a robust `max(finish_time_A, start_time_B)` bounds check to seamlessly handle the physical reality of waiting for a ride to open versus arriving after it has already started operating.

**2161. Partition Array According to Given Pivot**: Avoids the unstable relative-ordering destruction of the classic $O(1)$ space Dutch National Flag algorithm. Utilizes a strict $O(N)$ stable bucket-placement strategy (or a highly optimized two-pass pre-allocated array) to guarantee chronological preservation of elements while grouping them cleanly around the pivot.

**2196. Create Binary Tree From Descriptions**: Merges Graph construction with Tree logic. Bypasses nested tree-traversal lookups by maintaining a central Hash Map of memory references `(val -> TreeNode)`. It identifies the ultimate Root node in $O(N)$ time by simply tracking all valid children in a Hash Set and returning the singular orphaned parent. Space-optimized variants inject a `has_parent` boolean directly into the instance `__dict__` to eliminate the Hash Set memory footprint entirely.

**1189. Maximum Number of Balloons**: Leverages Python's `collections.Counter` to construct an $O(N)$ single-pass frequency map of the input text. It derives the maximum possible instances of the target word by mathematically scaling down double-occurrence characters (`'l'` and `'o'` via integer division `// 2`) and returning the strict minimum across the five-character requirement pool.

**3020. Find the Maximum Number of Elements in Subset**: Transforms a complex subset pattern recognition prompt into a straightforward frequency map traversal. By recognizing that valid sequences form a symmetrical mountain of squared bases ($x \rightarrow x^2 \rightarrow x^4$), it counts element pairs to build the upward and downward slopes. It isolates the infinite-loop trap of base $1$ by independently extracting its odd frequency bound, solving the entire array in an optimal $O(N)$ sweep.

**1846. Maximum Element After Decreasing and Rearranging**: Marks the **50th Medium Problem** solved! Bypasses standard $O(N \log N)$ sorting overhead by recognizing that the maximum possible answer in an array of size $N$ is strictly bounded by $N$. Utilizes an $O(N)$ frequency bucket array to clamp oversized elements, dynamically building the maximum possible staircase height in a single linear sweep.

**1967. Number of Strings That Appear as Substrings in Word**: Demonstrates the power of idiomatic Python by bypassing manual sliding-window character matching. Leverages Python's native `in` operator—backed by highly optimized C-level string search algorithms—to evaluate substring existence across the pattern array in practically instant sub-linear time, maintaining a strict $O(1)$ memory footprint.

**1358. Number of Substrings Containing All Three Characters**: Bypasses the overhead of a traditional shrinking sliding window by implementing Last-Seen Index Tracking. By recording the most recent occurrence of each required character in an array, the minimum of these indices acts as a strict bottleneck. This reveals that every index from 0 up to this minimum is a valid starting position, allowing the algorithm to mathematically accumulate the correct counts in a lightning-fast $O(N)$ linear sweep.

**3754. Concatenate Non-Zero Digits and Multiply by Sum I**: Solves a multi-step integer transformation cleanly in O(D) time (where D is the number of digits). By converting the integer to a string to filter out zeroes and immediately utilizing Python's generator expressions for the digit sum, it achieves an ultra-lean linear scan while avoiding repeated arithmetic division and modulo operations.

**1291. Sequential Digits**: Bypasses the catastrophic $O(N)$ Time Limit Exceeded (TLE) error of manually validating sequential elements across massive boundary limits (up to $10^9$). By recognizing that every possible valid answer is strictly a substring of the mathematical master string `"123456789"`, the algorithm restricts the entire search space to a universally bounded maximum of 36 checks, generating and naturally sorting the results in absolute $O(1)$ constant time.

**3658. GCD of Odd and Even Sums**: Bypasses the $O(N)$ execution trap of simulating odd and even arrays entirely. Utilizing mathematical proofs, it recognizes that the sum of the first $n$ odd numbers is exactly $n^2$ and the first $n$ even numbers is exactly $n(n+1)$. Because $n$ and $n+1$ are consecutive integers, their Greatest Common Divisor is strictly $1$. Thus, $\gcd(n^2, n(n+1))$ mathematically collapses directly to $n$, reducing the entire algorithm to a pure $O(1)$ constant-time return statement.

**3867. Sum of GCD of Formed Pairs**: Translates a multi-step array transformation into an ultra-lean execution by utilizing in-place memory mutation. Instead of allocating a secondary `prefixGcd` array, it tracks the running maximum and instantly overwrites the original indices with their evaluated GCDs. A standard sorting operation paired with a shrinking two-pointer boundary allows it to pair minimum and maximum elements seamlessly, mathematically sidestepping the unpaired middle element during odd-length constraints by terminating strictly when `left < right`.

**1979. Find Greatest Common Divisor of Array**: Demonstrates optimal boundary extraction by bypassing standard $O(N \log N)$ array sorting. Utilizes a strict $O(N)$ dual-linear scan via built-in `min()` and `max()` functions to instantly isolate the target elements. Evaluates the resulting pair utilizing the mathematical Euclidean algorithm (`math.gcd`), resolving the greatest common divisor in highly optimized logarithmic time while maintaining an absolute $O(1)$ auxiliary memory footprint.

**1260. Shift 2D Grid**: Marks the phenomenal **120th Problem Milestone**! Bypasses the complex conditional logic of simulating 2D matrix wrap-arounds by treating the matrix as a continuous 1D cyclic array. By applying an inverse modulo transformation `(curr_1D - k) % TOTAL`, the algorithm mathematically queries the origin of every cell in a single $O(M \times N)$ sweep. The heavily optimized Pythonic variant achieves the exact same result in three lines of code by executing raw C-level list slicing and reshaping.

**3499. Maximize Active Section with Trade I**: Deconstructs a complex, multi-stage block transformation rule into an ultra-lean $O(N)$ linear sweep. Utilizing the "1-Refund Illusion," the algorithm recognizes that sacrificing an active block perfectly merges the adjacent inactive blocks, and immediately refunds the sacrificed elements when the newly formed superstructure is converted back. This mathematical guarantee reduces the logic to simply finding the maximum sum of any two adjacent inactive blocks and appending it to the original active base count.

**3536. Maximum Product of Two Digits**: Marks the incredible **125th Problem Milestone**! Bypasses the $O(d^2)$ redundant evaluations of testing pairwise digit combinations by recognizing that the maximum product strictly relies on the two largest numerical digits present in the integer. The Pythonic implementation achieves this in $O(d \log d)$ time via string conversion and sorting, while the bare-metal math variant executes in strictly $O(d)$ time and $O(1)$ auxiliary space by peeling digits from right to left using modulo arithmetic (`% 10`) and maintaining a running dual-champion tracker.

**628. Maximum Product of Three Numbers**: Bypasses the combinatorial overhead of checking all possible triplets by mathematically analyzing the sign-flipping properties of integer multiplication. Because the product of two negative numbers yields a positive scalar, the maximum possible product is guaranteed to be either the three largest elements (`max1 * max2 * max3`) or the two smallest negative elements multiplied by the largest element (`min1 * min2 * max1`). The Pythonic solution resolves this in $O(N \log N)$ via sorting, while the optimal bare-metal variant executes in strictly $O(N)$ time and $O(1)$ auxiliary space by sweeping the array once with a five-variable extreme value tracker.

**1464. Maximum Product of Two Elements in an Array**: Completes the extreme-value product trilogy by evaluating array pairs under a decremented transformation. Because problem constraints guarantee strictly positive integers ($nums[i] \ge 1$), subtracting $1$ preserves order monotonicity without introducing negative-sign inversion traps. The algorithm bypasses $O(N^2)$ pairwise evaluations entirely, using an optimal $O(N)$ single-pass linear scan with a dual-champion tracker to isolate the two largest elements in constant $O(1)$ auxiliary memory.

**3517. Smallest Palindromic Rearrangement I**: Bypasses the computational overhead of combinatorial string permutations by exploiting the guaranteed symmetry of palindromic inputs. Because character frequencies remain invariant under permutation, any character exhibiting an odd frequency is mathematically bounded to the center index. The algorithm executes an optimal $O(N)$ frequency scan, constructs the lexicographically smallest left prefix using integer division (`count // 2`) across sorted character keys, and mirrors the prefix in constant time to construct the final palindrome.

**3014. Minimum Number of Pushes to Type Word I**: Demonstrates an elegant greedy simplification by capitalizing on the guarantee of unique characters. Bypassing character frequency analysis entirely, the algorithm mathematically distributes the string's length across 8 available hardware keys tier-by-tier. This abstraction reduces string processing to a pure mathematical constant-time execution utilizing integer division and boundary constraints.

**3731. Find Missing Elements**: Bypasses the $O(N \log N)$ penalty of array sorting by capitalizing on the implicit boundaries given in the constraints. By converting the input array into a Hash Set for $O(1)$ constant-time lookups, the algorithm efficiently sweeps the exact bounded integer range (`min(nums)` to `max(nums)`), appending missing elements in a naturally sorted order. The alternative Pythonic one-liner leverages optimized C-backend set difference operations (`set(range) - set(nums)`) for extreme syntactical elegance.

**3345. Smallest Divisible Digit Product I**: Showcases how mathematical boundary analysis reduces an apparently unbounded `while` loop into a strict $O(1)$ constant-time execution. By identifying the "Zero-Digit Ceiling," the algorithm recognizes that incrementing `n` will inherently produce a trailing zero within at most 10 iterations. Since a zero-digit cascades the multiplicative product to $0$—which satisfies any modulo target $t$—the execution strictly bypasses the risk of Time Limit Exceeded (TLE) errors using space-optimized in-place digit peeling (`n % 10`).

**2996. Smallest Missing Integer Greater Than Sequential Prefix Sum**: Showcases an optimal multi-stage array parsing mechanism. The algorithm utilizes an O(N) linear sweep with a conditional early exit (`nums[i] != nums[i - 1] + 1`) to isolate the strictly sequential prefix sum constraint. It subsequently bypasses the catastrophic O(N^2) overhead of iteratively searching the array for the calculated sum by injecting all elements into a Hash Set, resolving the final missing integer via O(1) constant-time lookups.

**3090. Maximum Length Substring With Two Occurrences**: Achieves optimal $O(N)$ traversal by implementing a classic dynamically shifting Sliding Window. Serving as the string-based Easy counterpart to Problem 2958, the algorithm leverages a dual-pointer mechanism backed by a constant-space $O(1)$ Hash Map. When a character's frequency violates the hardcoded threshold (`count > 2`), the left boundary efficiently contracts until validity is restored, isolating the absolute maximum contiguous block without requiring $O(N^2)$ brute-force sub-string extraction.

**3702. Longest Subsequence With Non-Zero Bitwise XOR**: Showcases the mathematical beauty of the XOR operation's self-canceling properties. Bypassing massive subset generation ($O(2^N)$), the algorithm evaluates the global XOR sum in a strictly $O(N)$ linear pass. It leverages the proof that if the global XOR is $0$, extracting any single non-zero element mathematically guarantees the remaining subset will equal that extracted element ($0 \oplus x = x$), yielding a maximal subsequence length of exactly $N - 1$.

**3471. Find the Largest Almost Missing Integer**: Showcases an intuitive moving-window hashing technique to track localized element presence. Bypassing global frequency constraints, the algorithm extracts unique values per window using $O(K)$ hash sets, dynamically tallying subarray-specific occurrences into a global map. A final constant-space sweep isolates the maximal valid element, resolving the localized existence condition gracefully in $O(N \times K)$ time.

**3069. Distribute Elements Into Two Arrays I**: Showcases a clean and optimal list simulation. By leveraging Python's `O(1)` list tail lookups (`arr[-1]`), the algorithm completely avoids scanning array contents or tracking auxiliary pointers. Elements are continuously appended to the correct sub-list based on instant peak-value comparisons, followed by a final `O(N)` list concatenation.

### Complex Logic

**3013. Divide Array... Min Cost II**: A Hard problem tackled using a Dual Heap (Min/Max) approach to maintain a sliding window of the smallest k elements efficiently.  

**3640. Trionic Array II**: Uses a state machine approach to track multiple DP states (ascent, descent, final ascent) simultaneously, optimizing for scenarios with negative numbers.  

**761. Special Binary String**: A beautiful algorithmic trick that treats special binary strings exactly like valid parentheses. Uses recursion to peel back the "brackets", sort the inner independent blocks, and glue them back together for the lexicographically largest result.

**3721. Longest Balanced Subarray II**: A serious step up from Version I. Uses a Segment Tree with lazy propagation and prefix sums to efficiently manage and query huge array ranges in O(n log n) time.

**3666. Minimum Operations to Equalize Binary String**: A Biweekly Contest Hard problem. Bypasses strict Time Limit Exceeded (TLE) errors in a BFS state-space search by utilizing a `SortedList` and tracking zero-count parities, dropping the lookup time to $O(\log N)$.

**1545. Find Kth Bit in Nth Binary String**: Avoids generating a massive, million-character binary string by treating the sequence generation as a mirror. Uses $O(N)$ recursive Divide & Conquer to mathematically track the position through mirrored and inverted halves.

**1888. Minimum Number of Flips to Make the Binary String Alternating**: Solves a complex cyclic-shift problem using a Sliding Window. Instead of physically reallocating memory to shift characters or doubling the string (`s + s`), it achieves $O(1)$ auxiliary space by using modulo arithmetic (`i % n`) to create a "virtual" doubled string.

**1980. Find Unique Binary String**: Showcases a brilliant implementation of Cantor's Diagonalization argument. Instead of generating and searching through a massive O(2^N) state space, it constructs a guaranteed unique string in strict O(N) time by simply flipping the i-th bit of the i-th string, mathematically proving uniqueness without a single collision check.

**3129. Find All Possible Stable Binary Arrays I**: Optimizes a complex combinatorial problem down to an $O(Z \times O)$ time complexity using bottom-up Dynamic Programming. Instead of using an inner loop to validate block sizes, it achieves $O(1)$ state transitions by mathematically subtracting the exact number of invalid sequences that just exceeded the consecutive character `limit`.

**1415. The k-th Lexicographical String of All Happy Strings of Length n**: Bypasses the standard $O(2^N)$ backtracking generation by using Combinatorics. It calculates the exact branch of the decision tree the $k$-th string resides in at every character position, effectively predicting the entire path in strict $O(N)$ time.

**3130. Find All Possible Stable Binary Arrays II**: Scales the mathematical state subtraction logic to handle Hard constraints (over 1,000,000 DP states). By decoupling a heavy 3D matrix into two independent 2D arrays (`dp0` and `dp1`), this architectural tweak drastically reduces Python's memory allocation overhead and pointer-chasing latency, allowing the algorithm to comfortably beat strict Time Limit Exceeded (TLE) constraints.

**1622. Fancy Sequence**: Bypasses the need for a heavy Segment Tree with lazy propagation by leveraging Affine Transformations ($y = mx + c$) and Fermat's Little Theorem. Instead of updating $10^5$ array elements on every API call, it modifies the global state in $O(1)$ time, applying a modular inverse to "pre-shrink" newly appended values so they correctly align with future global transformations.

**1727. Largest Submatrix With Rearrangements**: Transforms a chaotic 2D matrix rearrangement problem into a classic histogram area problem. By calculating consecutive vertical 1s in-place and greedily sorting each row's heights, it completely bypasses the need for combinatorial column shuffling, finding the optimal area in $O(M \cdot N \log N)$ time.

**3070. Count Submatrices with Top-Left Element and Sum Less Than k**: Bypasses the strict $O(M \times N)$ execution time by applying a spatial "Staircase Pruning" technique to a 2D Prefix Sum. By realizing that extending a matrix across non-negative integers guarantees a monotonic increase in sum, it aggressively shrinks the column iteration boundaries the moment a sum exceeds $k$, dropping the real-world time complexity closer to $O(\text{Valid Matrices} + M)$.

**3212. Count Submatrices With Equal Frequency of X and Y**: Implements a 2D Prefix Sum without allocating a full $O(M \times N)$ auxiliary matrix or mutating the input data. By tracking a running horizontal row count and cumulatively adding it to a 1D vertical column array, it successfully evaluates all top-left submatrices while minimizing the space complexity to a strict $O(N)$.

**3567. Minimum Absolute Difference in Sliding Submatrix**: Demonstrates constraint-driven algorithm selection. Instead of over-engineering a complex 2D rolling window or utilizing balanced BSTs, it leverages the microscopic grid constraints ($N \le 30$) to deploy an ultra-lean $O(M \cdot N \cdot K^2 \log K)$ brute-force submatrix extraction and sorting mechanism, optimizing for real-world execution speed over theoretical asymptotic bounds.

**1594. Maximum Non Negative Product in a Matrix**: Demonstrates the failure of greedy pathfinding algorithms when dealing with negative multiplication. It uses a 2D Dynamic Programming matrix to track dual-states (`max_product`, `min_product`) at every cell, successfully maintaining the lowest negative bounds to capitalize on sign-flipping operations further down the grid.

**2906. Construct Product Matrix**: Solves a 2D variation of the classic "Product Except Self" problem while navigating strict non-prime modulo constraints ($12345$). Because the modulo is non-prime, division via Modular Multiplicative Inverse is mathematically invalid. This solution elegantly bypasses the need for division entirely by flattening the matrix traversal into an $O(N \cdot M)$ two-pass algorithm, calculating running prefix and suffix products while updating the result matrix in-place for $O(1)$ auxiliary space.

**3546. Equal Sum Grid Partition I**: Bypasses the need for a heavy 2D Prefix Sum matrix by utilizing 1D Spatial Projection. Because valid cuts must span the entire length or width of the grid, the $O(M \times N)$ 2D matrix can be mathematically squashed into two independent 1D arrays (`row_sums` and `col_sums`). This reduces the partitioning logic to a trivial 1D running prefix sum check, drastically simplifying the codebase and boundary conditions.

**3548. Equal Sum Grid Partition II**: Bypasses severe Time Limit Exceeded (TLE) constraints by replacing heavy $O(N^2)$ graph-connectivity validation (BFS/DFS) with absolute topological properties. It leverages the mathematical proof that removing any single internal node from a $\ge 2 \times 2$ grid graph maintains its connected components, strictly limiting boundary-deletion checks to 1D isolated sub-vectors. This reduces the problem back to a highly-optimized $O(M \times N)$ frequency map sweep.

**2463. Minimum Total Distance Traveled**: Demonstrates advanced state optimization in Dynamic Programming. Rather than "flattening" the factory capacities into a massive 1D array—which risks catastrophic maximum recursion depth limits in Python—the algorithm utilizes Capacity Batching. At each factory state `f_idx`, a localized loop simulates assigning `k` robots at once. This drastically compresses the recursion tree depth to a strict maximum of $F$ (factories), ensuring safe, robust, and highly performant $O(R^2 \times F)$ execution.

**1320. Minimum Distance to Type a Word Using Two Fingers**: Bypasses the massive memory overhead of a 3D DP State (`index`, `finger_1`, `finger_2`) by utilizing State Compression. By recognizing that one finger is strictly bound to the spatial coordinate of `word[i-1]`, the algorithm compresses the state down to 2D (`index`, `other_finger`), dropping the time complexity drastically to an ultra-lean $O(N \times 27)$.

**2751. Robot Collisions**: Uses a stack to simulate real-time collisions after sorting by position. Left-moving robots sequentially crash into the stack of right-moving robots, handling health deductions and mutual destructions natively without creating a nested loop bottleneck.

**37. Sudoku Solver**: Avoids standard $O(N)$ row/col validation during Backtracking by utilizing 3 arrays of Hash Sets (`rows`, `cols`, `boxes`). This reduces the validity check for every digit placement down to a lightning-fast $O(1)$ lookup, drastically pruning the $O(9^M)$ decision tree.

**3027. Find the Number of Ways to Place People II**: Bypasses complex 2D Segment Trees by sorting coordinates (X ascending, Y descending) to guarantee directional logic. Uses a nested sweep that validates empty bounding boxes in strict $O(1)$ time by maintaining a "running highest Y-coordinate", instantly blocking any prospective rectangles that trap intermediate points.

**1340. Jump Game V**: Bypasses the complexity of full BFS array traversals by recognizing the downward jumping rule transforms the array into a Directed Acyclic Graph (DAG). Utilizes a Top-Down DFS with memoization to strictly calculate overlapping "line of sight" jumps in $O(N \cdot d)$ time, instantly breaking inner loops when a visual obstruction (a taller or equal element) is encountered.

**1871. Jump Game VII**: Prevents an $O(N \cdot K)$ Time Limit Exceeded (TLE) error by avoiding nested backwards lookups for valid jump origin points. Utilizes a Sliding Window variable (`reachable_in_window`) to maintain a rolling count of valid, active launchpads within the `[minJump, maxJump]` bounds, reducing the dynamic programming state transitions to a strictly $O(1)$ constant-time check per index.

**3635. Earliest Finish Time for Land and Water Rides II**: Solves the Time Limit Exceeded (TLE) barrier of its predecessor by abandoning the $O(N \times M)$ nested loop simulation. Instead, it utilizes an $O(N \log M)$ Binary Search paired with precomputed Prefix and Suffix Minimum arrays. This guarantees $O(1)$ optimal ride selection by instantly splitting the target ride pool into two distinct, pre-calculated mathematical bounds: rides requiring a wait time, and rides offering immediate boarding.

**3751. Total Waviness of Numbers in Range I**: Bypasses the catastrophic Time Limit Exceeded (TLE) of an $O(N)$ brute-force iterative scan by utilizing Digit Dynamic Programming. By constructing prefixes and tracking only the previous two digits in the recursive state, it evaluates the total topological waviness in $O(\log_{10}(\text{num2}))$ time. It calculates $F(num2) - F(num1 - 1)$ to isolate the target range with absolute mathematical precision.

**3753. Total Waviness of Numbers in Range II**: Because the $O(\log N)$ Digit DP architecture built for the Phase I version was already strictly optimal, it effortlessly clears the $10^{15}$ constraint boundary of this Hard variation. This demonstrates the power of state-space reduction—by evaluating mathematical digit transitions rather than iterating through integers, it resolves massive ranges in micro-seconds without requiring a single code modification.

**2574. Left and Right Sum Differences**: Eliminates the $O(N^2)$ overhead of recalculating subarray sums at every index. Utilizes a single-pass "Running Balance" algorithm that precalculates the total sum as the initial `right_sum`, dynamically shifting values to the `left_sum` in $O(1)$ time per step. The space-optimized variant successfully mutates the input array in-place, reducing the total memory footprint to strict $O(1)$ without sacrificing linear time execution.

**3558. Number of Ways to Assign Edge Weights I**: Disguises a pure combinatorics problem behind a standard Tree traversal prompt. Rather than simulating edge weight assignments or running pathfinding sum checks, it leverages mathematical parity. By proving that exactly half of all possible $1$ and $2$ weight assignments across $L$ edges result in an odd sum, the algorithm reduces the entire problem to a single $O(N)$ BFS depth discovery, followed by an $O(\log L)$ execution of $2^{L-1} \pmod{10^9+7}$.

**3699. Number of ZigZag Arrays I**: Bypasses the $O(N \cdot K^2)$ execution penalty of standard state-space DP by enforcing strict directional alternation (UP followed by DOWN). It flattens the transition calculations down to an optimal $O(N \cdot K)$ linear sweep by maintaining running prefix sums for valid UP-step origins and running suffix sums for valid DOWN-step origins, achieving an ultra-lean $O(K)$ space footprint.

**3700. Number of ZigZag Arrays II**: Overcomes the $N = 10^9$ Time Limit Exceeded (TLE) barrier of Phase I by shifting from iterative Dynamic Programming to Block Matrix Exponentiation. Because the transition rules between numbers are position-invariant, the entire recurrence is encoded into $M \times M$ transition matrices ($A$ for UP steps, $B$ for DOWN steps). Utilizing binary exponentiation to compute $(A \cdot B)^k$ in $O(\log N)$ steps, it successfully processes 1-billion element arrays in a fraction of a second.

**3737. Count Subarrays With Majority Element I**: Bypasses the $O(N \log N)$ Time Complexity trap of utilizing a Fenwick Tree (Binary Indexed Tree) or Merge Sort to count prefix inversions. By treating the target as $+1$ and all other elements as $-1$, it enforces a strict single-step differential. This allows the algorithm to maintain a running tally of valid historical prefix sums in pure $O(N)$ time by dynamically adding or subtracting the exact boundary frequency whenever the global sum ascends or descends.

**3739. Count Subarrays With Majority Element II**: Bypasses the $O(N \log N)$ execution overhead of utilizing a Fenwick Tree (Binary Indexed Tree) or Merge Sort to track prefix inversions across $10^5$ constraints. By transforming target elements into $+1$ and non-targets into $-1$, the algorithm reduces the majority condition to finding positive subarray sums. It maintains a running tally of valid historical prefix sums in pure $O(N)$ linear time by dynamically adding or subtracting the exact boundary frequency whenever the global running sum ascends or descends.

**2812. Find the Safest Path in a Grid**: Combines two advanced traversal algorithms to maximize a bottleneck condition. It executes a Multi-Source BFS to precompute the exact Manhattan distance from all threats simultaneously. To navigate the grid without invoking a standard $O(N^2 \log N)$ Binary Search bound-check, it employs a Dijkstra-style Max-Heap, dynamically prioritizing the safest available frontiers to guarantee the global optimal path is returned upon reaching the destination. The highly optimized variant achieves $O(N)$ auxiliary space by aggressively mutating the input grid to double as both the BFS distance map and the heap's visited tracker.

**3756. Concatenate Non-Zero Digits and Multiply by Sum II**: Bypasses the $O(Q \times M)$ Time Limit Exceeded (TLE) barrier of repeated string extraction over large query arrays. It performs string compression by filtering out zero digits—which contribute nothing to concatenation or sum—and precomputes modular prefix sums and powers of 10 over the remaining indices. This allows any arbitrary range query $[l, r]$ to map via binary search to its non-zero bounds, extracting the concatenated integer value and digit sum in $O(\log M)$ time per query.

**3312. Sorted GCD Pair Queries**: Bypasses the catastrophic $O(N^2)$ Time Limit Exceeded (TLE) error of generating and evaluating distinct array pairs. It mathematically resolves the frequencies of all possible GCDs by implementing an Inclusion-Exclusion Sieve. By tracking multiples and sweeping backward from the maximum value $M$, it subtracts overcounted higher-order multiples in $O(M \log M)$ time based on the harmonic series. It then aggregates these exact counts into a prefix sum array, answering massive arrays of sorted-index queries in $O(\log M)$ time per query via Binary Search.

**1081. Smallest Subsequence of Distinct Characters**: Bypasses the combinatorial nightmare of evaluating all valid subsequences by utilizing a Monotonic Stack. By pre-calculating the last occurrence index of every character, the algorithm greedily pops lexicographically larger characters off the stack whenever a smaller character is encountered—provided that the popped character is guaranteed to appear again later in the string. This reduces the entire problem to a highly efficient $O(N)$ linear scan, requiring only $O(1)$ auxiliary memory restricted to the 26-character alphabet.

**3513. Number of Unique XOR Triplets I**: Bypasses the catastrophic $O(N^3)$ Time Limit Exceeded (TLE) error of nested triplet simulation by capitalizing on the array's permutation properties. Recognizing that an input containing all integers from $1$ to $n$ can trivially generate $0$ (via $1 \oplus 2 \oplus 3 = 0$) and any original element $y$ (via $x \oplus x \oplus y = y$), the algorithm proves that valid triplets completely saturate the binary vector space up to $n$'s highest bit. This reduces the entire resolution to evaluating the power-of-two ceiling $2^k$ (where $k$ is the bit length of $n$), executing in strictly $O(1)$ constant time with zero auxiliary memory.

**3514. Number of Unique XOR Triplets II**: Marks the **60th Medium Problem Milestone**! Bypasses the catastrophic $O(N^3)$ Time Limit Exceeded (TLE) error of evaluating all three-element combinations by implementing a 2-Step Pairwise XOR Sieve. Capitalizing on the commutative properties of XOR and the constraint bounding $\text{nums}[i] \le 1500$, the algorithm first computes all achievable pairwise XORs into a bounded boolean array of size $2^{\lfloor \log_2(\max) \rfloor + 1} \le 2048$. It then combines these intermediate states with the unique elements of the array in a secondary linear pass, reducing the computational complexity from billions of operations down to an ultra-lean $O(U^2 + P \times U)$ execution time.

**3518. Smallest Palindromic Rearrangement II**: Marks the titanic **30th Hard Problem Milestone**! Bypasses the catastrophic $O(N!)$ combinatorial bottleneck of generating consecutive permutations by implementing an $O(N)$ Prefix Skipping mathematical model. By calculating the total subset permutations via the multinomial theorem, the algorithm evaluates positional character placement dynamically. If a character's subset permutations fall below the target $k$, the entire block is mathematically skipped ($k = k - \text{sub\_perms}$), bypassing millions of recursive branch calculations. The subset permutations are updated in strictly $O(1)$ time per placement via the relation $P_{new} = P_{old} \times \frac{count}{N}$, entirely avoiding iterative factorial recalculation.

**3016. Minimum Number of Pushes to Type Word II**: Expands on the hardware mapping abstraction of Part I by introducing character recurrence. To minimize global traversal costs across the 8-key matrix, the algorithm executes a complete $O(N)$ character frequency sieve utilizing a fixed 26-element array. By sorting the extracted frequencies descending in $O(1)$ constant time, the system greedily locks the highest-density characters to the shallowest key depths (`multiplier = i // 8 + 1`), bypassing the overhead of simulating specific character-to-key positional assignments entirely.

**486. Predict the Winner**: Deconstructs a two-player zero-sum game by implementing a Minimax Dynamic Programming model. By replacing independent dual-player score tracking with a singular "Net-Difference" recurrence relation (`max(nums[left] - dp(left+1), nums[right] - dp(right-1))`), the algorithm beautifully encapsulates optimal opponent simulation. Furthermore, it mathematically proves that for any array of even length, Player 1 possesses a deterministic winning strategy by manipulating parity boundaries, returning an immediate $O(1)$ evaluation for half of all possible inputs before executing the $O(N)$ space-optimized bottom-up DP matrix.

**877. Stone Game**: Serves as a perfect mathematical corollary to the Minimax algorithm constructed in *Predict the Winner*. By enforcing an even array length and an odd summation total, the problem's constraints inadvertently transform it from a dynamic programming sequence into a pure Game Theory parity puzzle. The algorithm recognizes that the first player can perpetually dictate the selection phase, forcing the opponent into a mathematically inescapable parity trap, resolving the entire problem in strictly $O(1)$ constant time without ever traversing the array.

**1406. Stone Game III**: Elevates the zero-sum Minimax DP architecture by introducing multi-branch sequential selection. By iterating backward from the terminal state, the algorithm evaluates up to three distinct extraction choices ($k \in \{1, 2, 3\}$), perpetually maximizing the current player's net score advantage against the opponent's optimized future state (`max(take - dp[i+k])`). The implementation subsequently refines the $O(N)$ linear array down to strict $O(1)$ constant auxiliary memory by employing a three-variable sliding window to track the cascading subproblem states.

**3310. Remove Methods From Project**: Models complex software dependency chains utilizing a two-phase Directed Graph traversal. The algorithm leverages an $O(V+E)$ Breadth-First Search (BFS) to map the transitive closure of the buggy node, isolating the "infected" subgraph. A subsequent $O(E)$ edge validation pass guarantees project stability by ensuring no external nodes depend on the isolated subgraph (`u ∉ suspicious ∧ v ∈ suspicious`), gracefully returning the exact remaining active methods.

**3348. Smallest Divisible Digit Product II**: Deconstructs an intensely constrained scaling problem utilizing Prime Factor filtration and constant-space Dynamic Programming. It algorithmically rejects invalid modulo targets harboring prime factors $>7$, mapping valid sub-targets into an ultra-fast 2D DP minimum-digit matrix (`dp[55][35]`). To bypass Time Limit Exceeded (TLE) errors native to Python interpreter overheads at $N = 10^5$, the algorithm precomputes the DP states to strictly guarantee $O(1)$ array lookups. Furthermore, it utilizes a mathematical "Fast-Forward" suffix generator to inject excess `'1'` characters in bulk ($O(1)$ array extensions), synthesizing the lexicographically smallest zero-free string without exhaustive recursive tracing.

**3302. Find the Lexicographically Smallest Valid Sequence**: Achieves absolute greedy optimality without backtracking by synthesizing a Right-to-Left Dynamic Programming "Safety Net." The algorithm first precomputes the rightmost spatial bounds for exact suffix subsequences in $O(N)$ time (`back[i]`). During the left-to-right greedy index selection, it authorizes the utilization of the single character mutation wildcard *only* if the DP array guarantees the existence of an exact suffix match bounded strictly after the current index (`back[i+1] > j`), yielding the lexicographically smallest index array in a single flawless $O(N)$ pass.

**1140. Stone Game II**: Expands the zero-sum Minimax DP architecture by introducing a dynamically scaling action window ($1 \le X \le 2M$). To avoid tracking dual independent player states, the algorithm utilizes a precalculated Suffix Sum array, mapping the global remainder of stones in $O(1)$ time. This allows the optimal localized choice to be resolved purely via opponent subversion (`suffix_sum[i] - dp(i + X, max(m, X))`). The cascading recursion evaluates all localized permutations, achieving global optimality within $O(N^3)$ computational time bounded by $O(N^2)$ memoized states.

**1510. Stone Game IV**: Re-engineers the Stone Game franchise by stripping away score maximization in favor of pure topological Game Theory survival. The algorithm deploys a 1D Bottom-Up Dynamic Programming array to evaluate combinatorial win-states (`dp[i]`). By recognizing that any move forcing the opponent into a known `False` state inherently renders the current state `True`, it greedily short-circuits evaluation paths. The transition loops are strictly bounded by integer square limits ($k^2 \le i$), gracefully bypassing absolute quadratic penalties to resolve massive $10^5$ stone constraints in highly optimized $O(N \sqrt{N})$ time.

**2958. Length of Longest Subarray With at Most K Frequency**: Achieves a highly optimal $O(N)$ traversal by implementing a dynamically shifting Sliding Window architecture. Bypassing catastrophic $O(N^2)$ brute-force sub-array evaluations, the algorithm couples a Right-expanding pointer with a Hash Map frequency tracker. When a localized frequency violates the threshold constraint `k`, a Left-contracting pointer dynamically evicts elements until validity is restored, isolating the absolute maximum contiguous block in a single continuous linear sweep.

**2213. Longest Substring of One Repeating Character**: Highlights the raw speed of a custom-built Segment Tree architecture. By abandoning string reallocation and $O(N)$ sequential scans, the algorithm encapsulates contiguous prefix/suffix length boundaries into node states. When a point-update mutates a character at $O(\log N)$ depth, the unwinding recursion automatically bridges matching adjacent chunk boundaries (`suff_len[left] + pref_len[right]`), recalculating the global longest continuous block dynamically while strictly bypassing Time Limit Exceeded (TLE) errors in Python by using flat parallel state arrays.

**2029. Stone Game IX**: Dismantles a combinatorial Game Theory trap by reducing array elements entirely to their modulo 3 parities. By recognizing that modulo `0` elements function strictly as turn-flippers, the algorithm establishes two mathematical constants in $O(N)$ time: if `c0` is even, Alice wins given minimum availability (`c1 > 0 and c2 > 0`); if `c0` is odd, Alice requires a structural imbalance (`abs(c1 - c2) > 2`) to absorb the opponent's tempo advantage. This completely bypasses recursive Minimax state generation for an absolute $O(1)$ space evaluation.

**1563. Stone Game V**: Approaches a constrained division Game Theory problem utilizing a Top-Down Divide and Conquer DP architecture. Bypassing catastrophic combinatorial overhead, the algorithm leverages an $O(N)$ precomputed Prefix Sum array to evaluate all localized subarray weights in strict $O(1)$ constant time. By iterating through all possible spatial pivots ($O(N)$ splits for $O(N^2)$ states), it executes a complete state-space exploration to maximize the current player's residual value, caching evaluations to resolve the entire structure optimally in $O(N^3)$ computational time.

**1386. Cinema Seat Allocation**: Bypasses the catastrophic Time Limit Exceeded (TLE) constraints of $10^9$ matrix rows by utilizing an implicit global tracker. The algorithm assumes maximal capacity across all $N$ rows, completely ignoring unreserved rows to achieve an optimal $O(M)$ time complexity. For reserved rows, it leverages highly efficient Bitwise integers to map seat occupancies, applying static block masks (`0b00111100`) coupled with Bitwise AND operations (`mask & left == 0`) to evaluate overlapping conflicts in strict $O(1)$ constant time.

**3116. Kth Smallest Amount With Single Denomination Combination**: Showcases an advanced fusion of Discrete Mathematics and boundary searching. Bypassing the $O(K)$ iteration limit completely, the algorithm flips the premise to query the mathematical frequency of multiples beneath an arbitrary ceiling $x$. By utilizing Bitmasking to precompute the Least Common Multiples (LCM) and mathematical signs for all $2^N$ combinations, it evaluates the precise count of valid amounts in $O(2^N)$ time using the Principle of Inclusion-Exclusion (PIE). Embedding this evaluation inside a logarithmic Binary Search strictly isolates the $k$-th exact value, crushing massive bounds up to $10^{11}$ in mere milliseconds.

### Tree Operations
**1382. Balance a Binary Search Tree**: Demonstrates a brilliant two-step approach to restructuring trees. Instead of complex pointer rotations, it harvests nodes via an O(n) In-Order Traversal to get a sorted array, then uses Divide-and-Conquer to mathematically rebuild a perfectly balanced BST from the middle out.

**3741. Minimum Distance Between Three Equal Elements II**: Optimized the triplet distance formula $abs(i - j) + abs(j - k) + abs(k - i)$ by recognizing that for sorted indices $i < j < k$, the expression simplifies to $2(k - i)$. This transformation allows the problem to be solved in a single linear pass using a Hash Map to track the index of the element from two occurrences prior, reducing the search space from $O(N^3)$ to $O(N)$.

**3501. Maximize Active Section with Trade II**: Elevates the greedy "1-Refund Illusion" from its predecessor by executing it over $Q$ arbitrary, independent range queries. To bypass the catastrophic $O(Q \times N)$ execution bottleneck of repeated block evaluation, it pre-parses the string into distinct positional blocks and evaluates all possible merge gains into an underlying array. By layering a Sparse Table over this array, it resolves any continuous Range Maximum Query (RMQ) in strictly $O(1)$ constant time. Paired with dual binary searches to isolate truncated boundary edges, the algorithm mathematically enforces the "two-block minimum" constraint, processing massive query arrays flawlessly in $O(\log M)$ time per query.

### Graph Operations
**3600. Maximize Spanning Tree Stability with Upgrades**: Combines Binary Search on the Answer with Kruskal's Algorithm. Instead of building a complex dynamic tree, it efficiently validates a target "stability" score by constructing a Spanning Tree using a Disjoint Set Union (DSU) and optimally budgeting edge upgrades.

**3532. Path Existence Queries in a Graph I**: Bypasses the overhead of constructing an adjacency list or executing complex Disjoint Set Union (DSU) tree operations by capitalizing on the array's sorted property. Because `nums` is sorted in non-decreasing order, valid graph edges strictly form contiguous horizontal clusters. The algorithm sweeps the array in a single $O(N)$ pass, incrementing a component ID whenever an adjacent difference exceeds `maxDiff`, allowing any arbitrary path query $[u, v]$ to be evaluated in $O(1)$ constant time via index ID comparison.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/bcyberly/LeetCode-Solutions-Python.git
cd LeetCode-Solutions-Python
```
### Run any solution locally
```
python Strings/0067_Add_Binary.py
```

## 🤝 Contributing

While this is my personal learning repository, I welcome:

⭐ Stars if you find it helpful

🐛 Issues for suggesting improvements

💬 Discussions about alternative approaches

## 📅 Daily Commitment

I solve and commit at least one problem daily. Check the commits to see my progress!

### ⭐ Star this repo if you find it useful!
*Happy Coding! 🚀*