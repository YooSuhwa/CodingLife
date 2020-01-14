'''
   @ 2020/01/13 ush
   * 백준 알고리즘 - 2293 동전 1 (https://www.acmicpc.net/problem/2293)
   * python

   * dp

   * n가지 종류의 각각 다른 가치를 가진 동전이 있을 때, 그 가치의 합이 k원이 되도록 하는 경우의 수 구하기
   * '15989 1,2,3 더하기 4'문제와 동일한 dp 알고리즘
'''
size, n = map(int, input().strip().split(' '))
seq = [int(input()) for _ in range(size)]

dp = [0] * (n+1)
dp[0] = 1

for i in range(0, size):
    for j in range(1, n + 1):
        if j - seq[i] >= 0:
            dp[j] += dp[j - seq[i]]

print(dp[n])