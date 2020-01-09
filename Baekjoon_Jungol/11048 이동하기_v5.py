'''
   @ 2020/01/09 ush
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * (1,1) 에서 (n,m)으로 이동하려고 한다. 
   * 이동할 수 있는 방향은 오른쪽(i,j+1), 왼쪽(i+1, j), 오른쪽아래 대각선(i+1, j+1)이다.
   * map의 각 칸에 사탕이 주어져 있을 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

   * v5) (i,j)에서 시작 - 으로 점화식 변경
   	* v1~4) dp[i][j] = (i,j)로 이동했을 때, 가져올 수 있는 최대 사탕 개수
   	* v5) dp[i][j] = (i,j)로 이동을 시작했을 때, 가져올 수 있는 최대 사탕 개수
'''
import sys
sys.setrecursionlimit(1000000)
def go(i, j):
    if i >n or j >m :
        return 0

    if dp[i][j] >=0 :
        return dp[i][j]

    dp[i][j] = max(go(i+1, j), go(i, j+1)) + map[i][j]
    return dp[i][j]


n, m = map(int, input().strip().split(' '))
map = [[0]*(m+1)]+ [[0]+list(map(int,input().split())) for _ in range(n)]
dp = [[-1]*(m+1) for _ in range(n+1)]

print(go(1,1))