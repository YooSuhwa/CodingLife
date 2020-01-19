'''
   @ 2020/01/19 ush
   * 백준 알고리즘 - 12865 평범한 배낭 (https://www.acmicpc.net/problem/12865)
   * python

   * dp

   * n 개의 물건은 각각 무게 w와 가치 v를 가지고, 가방에는 최대 k무게까지만 넣을 수 있을 때, 가방에 넣을 수 있는 물건들의 가치 최대값을 구하는 프로그램
   * dp[i][j] = i번째 물건까지 고려하고, 배낭의 무게 합이 j 일 때, 가치의 최대값
   	* 1. i번째 물건을 가방에 넣지 않은 경우 : dp[i-1][j]
   	* 2. i번째 물건을 가방에 넣은 경우 : dp[i-1][j-w[i]] + v[i]  
   		== i가 빠졌을 때 + i의 가치 
'''
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