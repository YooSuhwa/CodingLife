'''
   @ 2020/01/15 ush
   * 백준 알고리즘 - 2294 동전 2 (https://www.acmicpc.net/problem/2294)
   * python

   * dp

   * n가지 종류의 각각 다른 가치를 가진 동전이 있을 때, 그 가치의 합이 k원이 되도록 하는 최소의 동전 개수 찾기
'''
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