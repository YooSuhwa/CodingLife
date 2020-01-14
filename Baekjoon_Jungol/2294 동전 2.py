size, n = map(int, input().strip().split(' '))
seq = [int(input()) for _ in range(size)]

dp = [-1] * (n+1)
dp[0] =0

for i in range(0, size):
    for j in range(1, n + 1):
        temp = j - seq[i]
        if temp >= 0 and dp[temp] != -1:
            if dp[j] == -1 or dp[j]> dp[temp]+1:
                dp[j] = dp[temp] + 1


print(dp[n])