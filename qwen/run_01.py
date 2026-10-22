import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]
    
    # dp[c][r] stores the maximum bitwise AND achievable using c elements with sum % M == r
    # Initialize with -1 (unreachable)
    dp = [[-1] * M for _ in range(K + 1)]
    # Base case: 0 elements chosen, neutral mask for bitwise AND (all 30 bits set)
    dp[0][0] = (1 << 30) - 1
    
    for x in A:
        rem_x = x % M
        # Iterate backwards to avoid using the same element multiple times
        for c in range(K - 1, -1, -1):
            for r in range(M):
                if dp[c][r] != -1:
                    new_val = dp[c][r] & x
                    new_rem = (r + rem_x) % M
                    if new_val > dp[c + 1][new_rem]:
                        dp[c + 1][new_rem] = new_val
                        
    print(dp[K][0])

if __name__ == '__main__':
    solve()
