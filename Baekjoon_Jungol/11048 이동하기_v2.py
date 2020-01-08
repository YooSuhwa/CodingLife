n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[0]*m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        if j + 1 < m and dp[i][j+1] < dp[i][j] + map[i][j+1]:
            dp[i][j + 1] = dp[i][j] + map[i][j + 1]
        if i + 1 <n and dp[i+1][j] < dp[i][j] + map[i+1][j]:
            dp[i+1][j] = dp[i][j] + map[i+1][j]
        if i + 1 < n and j + 1 < m and dp[i+1][j+1] < dp[i][j] + map[i+1][j+1]:
            dp[i+1][j + 1] = dp[i][j] + map[i+1][j + 1]

print(dp[n-1][m-1]+1)

