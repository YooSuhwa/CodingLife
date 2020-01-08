'''
   @ 2020/01/08 ush
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * (1,1) 에서 (n,m)으로 이동하려고 한다. 
   * 이동할 수 있는 방향은 오른쪽(i,j+1), 왼쪽(i+1, j), 오른쪽아래 대각선(i+1, j+1)이다.
   * map의 각 칸에 사탕이 주어져 있을 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

   * v3) 대각선 이동은 처리하지 않아도 된다는 아이디어
   	* A[i][j] >= 0 이라는 조건이 있으므로 대각선 이동은 다른 2가지(오른쪽>>아래 or 왼쪽 아래)를 포함한 방법보다 항상 작거나 같다
    * 따라서 v1에서 max 안 비교 중 대각선 빼주기
'''
n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[0]*m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + map[i][j]

print(dp[n-1][m-1])