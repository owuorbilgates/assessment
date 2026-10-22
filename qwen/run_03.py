import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]
    
    def can_pick_with_sum(elements):
        if len(elements) < K:
            return False
        dp = [[False] * M for _ in range(K + 1)]
        dp[0][0] = True
        for x in elements:
            rem = x % M
            for c in range(K - 1, -1, -1):
                for r in range(M):
                    if dp[c][r]:
                        dp[c + 1][(r + rem) % M] = True
        return dp[K][0]
    
    if not can_pick_with_sum(A):
        print("-1")
        return
        
    ans = 0
    # Attempt 3: Check each bit independently to avoid DP state explosion
    for bit in range(29, -1, -1):
        filtered = [x for x in A if (x & (1 << bit))]
        if can_pick_with_sum(filtered):
            ans |= (1 << bit)
            
    print(ans)

if __name__ == '__main__':
    solve()
