
testcase = int(input())

for _ in range(testcase):
    n = int(input())
    dp = [0] * (n+1)

    size = 3
    seq = (1,2,3)
    dp[0] = 1

    for i in range(0, size):
        for j in range(1, n+1):
            if j-seq[i] >= 0:
                dp[j] += dp[j - seq[i]]

    print(dp[n])