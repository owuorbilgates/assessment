import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]

    if K > N:
        print(-1)
        return

    def is_feasible(candidates, k, m):
        n_cand = len(candidates)
        if n_cand < k:
            return False
        
        dp = [[False] * m for _ in range(k + 1)]
        dp[0][0] = True
        
        for val in candidates:
            v_mod = val % m
            for c in range(min(k, n_cand), 0, -1):
                for r in range(m):
                    if dp[c-1][(r - v_mod) % m]:
                        dp[c][r] = True
                        
        return dp[k][0]

    if not A:
        print(-1)
        return
        
    max_val = max(A)
    if max_val == 0:
        if N >= K:
            print(0)
        else:
            print(-1)
        return
            
    max_bit = max_val.bit_length()
    ans = 0
    
    for b in range(max_bit - 1, -1, -1):
        candidate = ans | (1 << b)
        valid_elements = [x for x in A if (x & candidate) == candidate]
        if is_feasible(valid_elements, K, M):
            ans = candidate
            
    if not is_feasible(A, K, M):
        print(-1)
        return
        
    print(ans)

if __name__ == '__main__':
    solve()
