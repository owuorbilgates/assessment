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

    # dp[c][r] = maximum bitwise AND achievable by choosing c elements with sum % M == r
    # Initialize with -1 meaning impossible
    NEG_INF = -1
    dp = [[NEG_INF] * M for _ in range(K + 1)]
    dp[0][0] = (1 << 60) - 1  # AND of empty set is all 1s (identity for AND)

    for v in A:
        # Process in reverse to avoid using same element twice
        for c in range(min(K, N), 0, -1):
            for r in range(M):
                prev_r = (r - v) % M
                if dp[c - 1][prev_r] != NEG_INF:
                    new_and = dp[c - 1][prev_r] & v
                    if new_and > dp[c][r]:
                        dp[c][r] = new_and

    result = dp[K][0]
    print(result if result != NEG_INF else -1)

if __name__ == '__main__':
    solve()
