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
    
    # dp[c][r] = set of all possible AND values achievable by choosing c elements with sum % M == r
    dp = [[set() for _ in range(M)] for _ in range(K + 1)]
    # Base case: 0 elements chosen, sum remainder 0, AND value is all 1s (identity for AND)
    ALL_ONES = (1 << 32) - 1
    dp[0][0].add(ALL_ONES)
    
    for v in A:
        # Process in reverse order of count to avoid using the same element multiple times
        for c in range(min(K, N), 0, -1):
            for r in range(M):
                prev_r = (r - v) % M
                if dp[c - 1][prev_r]:
                    new_ands = set()
                    for old_and in dp[c - 1][prev_r]:
                        new_ands.add(old_and & v)
                    dp[c][r].update(new_ands)
    
    if not dp[K][0]:
        print(-1)
        return
    
    print(max(dp[K][0]))

if __name__ == '__main__':
    solve()
