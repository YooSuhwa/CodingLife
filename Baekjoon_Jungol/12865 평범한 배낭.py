n, k = map(int, input().strip().split(' '))
prod = [[0,0]]+[list(map(int,input().split())) for _ in range(n)]
n+= 1
k+= 1

dp = [[0] * k for _ in range(n)]

for i in range(1, n):
    for j in range(1, k):
        dp[i][j] = dp[i-1][j]

        if j - prod[i][0] >= 0:
            dp [i][j] = max(dp[i][j], dp[i-1][j-prod[i][0]]+ prod[i][1])

print(dp[n-1][k-1])