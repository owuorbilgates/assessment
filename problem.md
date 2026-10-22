# Modulo AND-Subsequence

## Problem Statement
You are given an array $A$ of $N$ non-negative integers, and two integers $K$ and $M$. 
You must choose exactly $K$ distinct elements from the array to form a subsequence. 
Your goal is to maximize the **bitwise AND** of these $K$ chosen elements, subject to the condition that the **sum** of these $K$ elements is a multiple of $M$ (i.e., $\text{sum} \equiv 0 \pmod M$).

If it is impossible to choose exactly $K$ elements such that their sum is a multiple of $M$, output `-1`.

## Input Format
- The first line contains three integers $N$, $K$, and $M$ ($1 \le K \le N \le 100$, $1 \le M \le 20$).
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ ($0 \le A_i < 2^{30}$).

## Output Format
- Print a single integer: the maximum bitwise AND of a valid $K$-element subsequence whose sum is a multiple of $M$, or `-1` if no such subsequence exists.

## Constraints
- $1 \le K \le N \le 100$
- $1 \le M \le 20$
- $0 \le A_i < 2^{30}$

## Examples

### Example 1
**Input:**
```
5 3 3
15 14 11 12 7
```

**Output:**
```
6
```

**Explanation:**
We must choose $K = 3$ elements whose sum is divisible by $M = 3$.
Consider the subset $[15, 14, 7]$:
- Sum: $15 + 14 + 7 = 36$, and $36 \equiv 0 \pmod 3$.
- Bitwise AND: $15 \ \& \ 14 \ \& \ 7 = 1111_2 \ \& \ 1110_2 \ \& \ 0111_2 = 0110_2 = 6$.

Other subsets of size 3 with sum divisible by 3 include:
- $[14, 12, 7]$: Sum $= 33 \equiv 0 \pmod 3$, AND $= 14 \ \& \ 12 \ \& \ 7 = 4$.
- $[15, 11, 7]$: Sum $= 33 \equiv 0 \pmod 3$, AND $= 15 \ \& \ 11 \ \& \ 7 = 3$.
- $[11, 12, 7]$: Sum $= 30 \equiv 0 \pmod 3$, AND $= 11 \ \& \ 12 \ \& \ 7 = 0$.

No valid 3-element subset yields a bitwise AND greater than 6. Thus, the answer is 6.

### Example 2
**Input:**
```
4 2 2
10 12 14 15
```

**Output:**
```
12
```

**Explanation:**
We must choose $K = 2$ elements whose sum is even ($M = 2$).
Choosing $[12, 14]$ gives:
- Sum: $12 + 14 = 26 \equiv 0 \pmod 2$.
- Bitwise AND: $12 \ \& \ 14 = 1100_2 \ \& \ 1110_2 = 1100_2 = 12$.

No valid pair yields a bitwise AND greater than 12.

### Example 3
**Input:**
```
5 5 2
1 1 1 1 1
```

**Output:**
```
-1
```

**Explanation:**
We must choose all 5 elements. Their sum is $1 + 1 + 1 + 1 + 1 = 5$, which is odd ($5 \not\equiv 0 \pmod 2$). Since no valid subset can be formed, the answer is -1.
