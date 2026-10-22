import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    K = int(input_data[1])
    M = int(input_data[2])
    A = [int(x) for x in input_data[3:3+N]]
    
    # Attempt 2: To fix optimal substructure failure, store reachable AND values in sets.
    # dp[c][r] stores a set of possible bitwise AND values using c elements with sum % M == r
    dp = [ [set() for _ in range(M)] for _ in range(K + 1) ]
    
    # Base case: 0 elements chosen, neutral mask for bitwise AND
    dp[0][0].add((1 << 30) - 1)
    
    for x in A:
        rem_x = x % M
        for c in range(K - 1, -1, -1):
            for r in range(M):
                if dp[c][r]:
                    new_rem = (r + rem_x) % M
                    for prev_and in dp[c][r]:
                        dp[c + 1][new_rem].add(prev_and & x)
                    # Heuristic pruning to prevent TLE/MLE
                    if len(dp[c + 1][new_rem]) > 64:
                        # Keep only the largest 64 elements
                        dp[c + 1][new_rem] = set(sorted(dp[c + 1][new_rem], reverse=True)[:64])
                        
    if not dp[K][0]:
        print("-1")
    else:
        print(max(dp[K][0]))

if __name__ == '__main__':
    solve()
