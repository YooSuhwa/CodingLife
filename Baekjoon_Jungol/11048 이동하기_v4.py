'''
   @ 2020/01/09 ush
   * 백준 알고리즘 - 11048 이동하기 (https://www.acmicpc.net/problem/11048)
   * python

   * dp

   * (1,1) 에서 (n,m)으로 이동하려고 한다. 
   * 이동할 수 있는 방향은 오른쪽(i,j+1), 왼쪽(i+1, j), 오른쪽아래 대각선(i+1, j+1)이다.
   * map의 각 칸에 사탕이 주어져 있을 때, 가져올 수 있는 사탕 개수의 최댓값을 구하는 프로그램

   * v4) 재귀함수로 구현하기
   	* v3의 Bottom-up 이중 포문을 go라는 재귀함수를 통해 Top-down으로 구현
'''
import sys
sys.setrecursionlimit(1000000) #런타임 에러 원인
def go(i, j):
    if i <1 or j <1 :
        return 0
    if dp[i][j] >=0 :
        return dp[i][j]

    dp[i][j] = max(go(i-1, j), go(i, j-1)) + map[i][j]
    return dp[i][j]

n, m = map(int, input().strip().split(' '))
m += 1
map = [[0]+list(map(int,input().split())) for _ in range(n)]
map = [[0]*m] + map
n += 1
dp = [[-1]*m for _ in range(n)]

print(go(n-1,m-1))