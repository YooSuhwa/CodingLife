def max3(n1, n2, n3):
    return max(max(n1, n2), n3)

n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[-1]*m for _ in range(n)]

for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max3(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + map[i][j]

print(dp[n-1][m-1]+1)