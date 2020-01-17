n = int(input())
n+=1
dp = [-1]*n
dp[0] = 0
for i in range(1,n):
    dp[i] = dp[i-1]+1
    for j in range(1,i-2):
        temp = dp[i-(j+2)]*(j+1)
        dp[i] = max(dp[i], temp)
print(dp[n-1])