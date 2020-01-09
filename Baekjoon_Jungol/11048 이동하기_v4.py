
def go(i, j):
    if i <0 or j <0 :
        return
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
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + map[i][j]


print(go(n-1,m-1)+1)