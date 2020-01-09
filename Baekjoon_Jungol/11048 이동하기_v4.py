import sys
sys.setrecursionlimit(1000000)
def go(i, j):
    if i <1 or j <1 :
        return 0
    if dp[i][j] >=0 :
        return dp[i][j]

    dp[i][j] = max(go(i-1, j), go(i, j-1)) + map[i][j]
    return dp[i][j]

n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[-1]*m for _ in range(n)]

print(go(n-1,m-1))