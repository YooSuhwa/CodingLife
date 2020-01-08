'''
   @ 2020/01/08 ush
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * (1,1) 에서 (n,m)으로 이동하려고 한다. 
   * 이동할 수 있는 방향은 오른쪽(i,j+1), 왼쪽(i+1, j), 오른쪽아래 대각선(i+1, j+1)이다.
   * map의 각 칸에 사탕이 주어져 있을 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

   * v2) 현재칸에서 갈 수 있는 경우의 수 살펴보기.
   	* 즉, 현재칸을 기준으로 현재칸이 갈 수 있는 3가지의 경로를 계산하기
'''
n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[0]*m for _ in range(n)]

for i in range(0, n):
    for j in range(0, m):
        if j + 1 < m:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + map[i][j + 1])
        if i + 1 <n :
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + map[i+1][j])
        if i + 1 < n and j + 1 < m :
            dp[i+1][j + 1] = max(dp[i+1][j + 1], dp[i][j] + map[i+1][j + 1])
print(dp[n-1][m-1])


