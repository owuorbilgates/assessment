import os
import sys
import random
import subprocess

# Seed for deterministic test case generation
random.seed(42)

os.makedirs('test_cases', exist_ok=True)

cases = []

# 1. Basic Example 1 (from problem.md)
cases.append("5 3 3\n15 14 11 12 7\n")

# 2. Basic Example 2 (from problem.md)
cases.append("4 2 2\n10 12 14 15\n")

# 3. Basic Example 3: Impossible sum (from problem.md)
cases.append("5 5 2\n1 1 1 1 1\n")

# 4. Edge Case: K = 1 (find largest element with A_i % M == 0)
cases.append("8 1 5\n12 15 20 7 25 31 10 4\n")

# 5. Edge Case: K = N (all elements must be selected)
cases.append("6 6 3\n63 63 63 63 63 63\n")

# 6. Edge Case: All zeros (sum % M == 0, AND = 0)
cases.append("5 3 4\n0 0 0 0 0\n")

# 7. Edge Case: M = 1 (sum modulo 1 is always 0, purely maximizes bitwise AND)
cases.append("10 4 1\n28 13 25 29 14 2 9 31 17 16\n")

# 8. Counterexample Trap 1: Flawed DP fails (returns 16 instead of 17)
cases.append("10 4 3\n28 13 25 29 14 2 9 31 17 16\n")

# 9. Counterexample Trap 2: Another bit-wise sub-optimal trapping case
cases.append("8 3 4\n24 16 15 7 11 19 27 23\n")

# 10. Impossible case: All elements == 1 mod M, but K % M != 0
cases.append("6 3 5\n1 6 11 16 21 26\n")

# 11. Random mid-size case
cases.append("10 5 7\n" + " ".join(str(random.randint(100, 1000000)) for _ in range(10)) + "\n")

# 12. Mid constraints with overlapping bit patterns
cases.append("20 8 6\n" + " ".join(str(random.randint(1, 255)) for _ in range(20)) + "\n")

# 13. Case where valid sum exists, but bitwise AND is 0
cases.append("10 5 3\n" + " ".join(str(1 << i) for i in range(10)) + "\n")

# 14. High bits cluster (testing bit 28-29 manipulation)
cases.append("100 10 20\n" + " ".join(str(random.randint(2**28, 2**29 - 1)) for _ in range(100)) + "\n")

# 15. Max constraints: N = 100, K = 50, M = 15
cases.append("100 50 15\n" + " ".join(str(random.randint(0, 2**29)) for _ in range(100)) + "\n")

# 16. Max constraints: N = 100, K = 100, M = 20
cases.append("100 100 20\n" + " ".join(str(random.randint(0, 2**29)) for _ in range(100)) + "\n")

# 17. Max constraints: N = 100, K = 1, M = 20
cases.append("100 1 20\n" + " ".join(str(random.randint(0, 2**29)) for _ in range(100)) + "\n")

# 18. Random case with large numbers close to 2^30 - 1
cases.append("50 20 17\n" + " ".join(str((2**30 - 1) - random.randint(0, 1024)) for _ in range(50)) + "\n")

# 19. Large sparse array with specific common masks
base_mask = (1 << 25) | (1 << 18) | (1 << 10) | (1 << 3)
sparse_vals = [base_mask | random.randint(0, 2**12) for _ in range(60)] + [random.randint(0, 2**20) for _ in range(20)]
random.shuffle(sparse_vals)
cases.append("80 30 13\n" + " ".join(str(x) for x in sparse_vals) + "\n")

# 20. Max constraints: N = 100, K = 90, M = 19
cases.append("100 90 19\n" + " ".join(str(random.randint(0, 2**29)) for _ in range(100)) + "\n")

print(f"Generating {len(cases)} test cases...")

py_cmd = sys.executable if sys.executable else "python3"

for i, stdin_data in enumerate(cases, 1):
    in_file = f'test_cases/{i}.in'
    out_file = f'test_cases/{i}.out'
    
    with open(in_file, 'w') as f:
        f.write(stdin_data)
        
    process = subprocess.run([py_cmd, 'solution.py'], input=stdin_data, text=True, capture_output=True)
    if process.returncode != 0:
        print(f"Error on case {i}: {process.stderr}")
        sys.exit(1)
        
    with open(out_file, 'w') as f:
        f.write(process.stdout)
        
    print(f"Test case {i} generated: output = {process.stdout.strip()}")

print("All test cases successfully generated!")
