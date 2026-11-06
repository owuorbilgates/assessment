# Modulo AND-Subsequence

This assignment asks for the maximum bitwise AND obtainable by choosing exactly
`K` distinct elements from an array, such that their sum is divisible by `M`.
Print `-1` if no such choice exists.

## Requirements

- Python 3
- No third-party packages

## Run

From the project directory, provide input on standard input:

```text
python solution.py
```

For example:

```text
5 3 3
15 14 11 12 7
```

The program prints one integer: the largest achievable AND, or `-1`.

## Input format

```text
N K M
A1 A2 ... AN
```

- `1 <= K <= N <= 100`
- `1 <= M <= 20`
- `0 <= Ai < 2^30`

## Algorithm

The solution greedily considers each bit from bit 29 down to bit 0. For each
candidate bit, it keeps only array elements that contain all bits selected so
far, then checks whether exactly `K` of those elements can have a sum congruent
to zero modulo `M`.

The feasibility check uses a Boolean dynamic-programming table indexed by the
number of selected elements and the current sum remainder. If the candidate
mask is feasible, the bit is included in the answer. A feasibility check with
an empty mask first detects when no valid selection exists.

- Time: `O(30 * N * K * M)`
- Space: `O(K * M + N)`

## Test data

`test_cases/` contains 20 input/output pairs (`1.in`/`1.out` through
`20.in`/`20.out`), including the examples and edge cases. Run an individual
case in PowerShell with:

```powershell
Get-Content test_cases\1.in | python solution.py
```

`generator.py` regenerates these cases and their expected outputs.
