import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]
    
    def can_achieve(target_mask):
        # Filter elements that have all bits of target_mask set
        F = [x for x in A if (x & target_mask) == target_mask]
        if len(F) < K:
            return False
        
        # DP to check if we can pick exactly K elements with sum % M == 0
        # dp[count][rem] is True if a subset of size count has sum % M == rem
        dp = [[False] * M for _ in range(K + 1)]
        dp[0][0] = True
        
        for val in F:
            rem_val = val % M
            # Iterate backwards over count to ensure each element is used at most once
            for c in range(K - 1, -1, -1):
                for r in range(M):
                    if dp[c][r]:
                        dp[c + 1][(r + rem_val) % M] = True
                        
        return dp[K][0]

    # First, check if ANY valid K-element subset exists whose sum is divisible by M
    if not can_achieve(0):
        print("-1")
        return

    ans = 0
    for bit in range(29, -1, -1):
        target = ans | (1 << bit)
        if can_achieve(target):
            ans = target
            
    print(ans)

if __name__ == '__main__':
    solve()
