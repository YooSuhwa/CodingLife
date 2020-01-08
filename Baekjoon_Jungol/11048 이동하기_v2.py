n, m = map(int, input().strip().split(' '))
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*(m+1)] + map
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if j + 1 <= m and dp[i][j+1] < dp[i][j] + map[i][j+1]:
            dp[i][j + 1] = dp[i][j] + map[i][j + 1]
        if i + 1 <=n and dp[i+1][j] < dp[i][j] + map[i+1][j]:
            dp[i+1][j] = dp[i][j] + map[i+1][j]
        if i + 1 <= n and j + 1 <= m and dp[i+1][j+1] < dp[i][j] + map[i+1][j+1]:
            dp[i+1][j + 1] = dp[i][j] + map[i+1][j + 1]

print(dp[n][m]+1)

