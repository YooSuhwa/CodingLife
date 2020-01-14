size, n = map(int, input().strip().split(' '))
seq = [int(input()) for _ in range(size)]

dp = [0] * (n+1)
dp[0] = 1

for i in range(0, size):
    for j in range(1, n + 1):
        if j - seq[i] >= 0:
            dp[j] += dp[j - seq[i]]

print(dp[n])